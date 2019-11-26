#!/usr/bin/env python3
import os
import shutil
import sys
import time
from collections import defaultdict

from dump_file import parse_dump_file
from rules import process_custom
from freeze_rules import get_rules


def print_usage():
    print("Usage: {} [thread dumps file]".format(os.path.basename(__file__)))


def extract_edt_call_stack(lines):
    """
    Extract EDT call stack from all dump
    :param lines: List[str] param. List of all file lines.
    :return: list of EDT stack trace calls
    """
    res = []
    in_edt = False
    before_ats = True
    for l in lines:
        if not in_edt:
            if "AWT-EventQueue" in l:
                in_edt = True
        else:
            if l.startswith("\tat "):
                before_ats = False
                res.append(l)
            elif not before_ats:
                if not l.strip():
                    break

    return res


def match_stack(stack):
    """
    Search EDT stack for known freeze described in FRAME_SEQ_TO_TICKET
    :param stack:
    :return:
    """
    if stack is not None:
        messages = set()
        for rule in get_rules():
            message = rule.is_matched(stack)
            if message:
                messages.add(message)
        if messages:
            return messages
        custom = process_custom(stack)
        if custom is not None:
            return {custom}
        else:
            return set()
    else:
        return set()


class ThreadDumpInfo:
    def __init__(self, file_name, messages, lines):
        self.file_name = file_name
        self.messages = messages
        self.lines = lines


def process_thread_dump(file_name, lines):
    """
    :param file_name:
    :param lines: List[str] param
    :return: ThreadDumpInfo
    """
    edt_stack = extract_edt_call_stack(lines)
    dump_info = parse_dump_file(lines)
    messages = match_stack(dump_info)
    return ThreadDumpInfo(file_name, messages, edt_stack)


def process_file(file_name):
    with open(file_name) as f:
        try:
            readlines = f.readlines()
        except (IOError, UnicodeError):
            readlines = []  # will be reported as "UNKNOWN"
        return process_thread_dump(file_name, readlines)


def get_summary(infos):
    all_tickets = defaultdict(int)
    detailed = []
    unknown = []
    for info in infos:
        if not info.messages:
            unknown.append(info.file_name)
        detailed.append(
            info.file_name + ": " + (", ".join(info.messages) if info.messages else "UNKNOWN") +
            "\n" +
            ("" if info.messages else ("\n" + "".join(info.lines) + "\n"))
        )
        for t in info.messages:
            all_tickets[t] += 1

    return "All found tickets:\n{}\nUnknown traces ({}):\n{}".format(
        tickets_to_string(all_tickets),
        len(unknown),
        "".join(detailed))


def tickets_to_string(all_tickets):
    return "\n".join(
        "   {}: {}".format(t, u) for t, u in sorted(all_tickets.items(), key=lambda k: (k[1], k[0]), reverse=True))


def collect_files(arg):
    if os.path.isfile(arg):
        if not os.path.basename(arg).startswith("."):
            yield arg
    elif os.path.isdir(arg):
        for folder_name, subfolders, filenames in os.walk(arg):
            if ".git" in folder_name:
                continue

            if filenames and 'threadDumps-freeze-20' in folder_name:
                # assume all freezes in this folder have the same cause
                yield folder_name + '/' + filenames[0]
            else:
                for f in filenames:
                    if not os.path.basename(f).startswith("."):
                        yield folder_name + '/' + f
    else:
        raise ValueError("Invalid file or folder: " + str(arg))


def parse_args_and_process_files(given_filenames):
    filenames = [f for arg in given_filenames for f in collect_files(arg)]
    infos = [process_file(f) for f in filenames]
    return get_summary(infos)


def write_to_otuput_dir(summary):
    output_dir = os.path.join(os.path.dirname(__file__), "out")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    result_file = "result-" + time.strftime("%Y%m%d-%H%M%S") + ".txt"
    with open(os.path.join(output_dir, result_file), "w") as out_file:
        out_file.writelines(summary)


def split_reports(filename, out_dir):
    with open(filename) as f:
        text = f.read()
    parts = text.split('==========')
    if os.path.exists(out_dir):
        shutil.rmtree(out_dir)
    os.makedirs(out_dir)
    for id, dump in zip(parts[0::2], parts[1::2]):
        with open(f'{out_dir}/{id.strip()}.txt', 'w+') as out_file:
            out_file.write(dump.replace('com.intellij.diagnostic.Freeze', 'AWT-EventQueue-0\njava.lang.Thread.State: RUNNABLE'))


def main():
    if len(sys.argv) < 2:
        print_usage()
    else:
        program_arguments = sys.argv[1:]
        if program_arguments[0] == '--split':
            split_reports(program_arguments[1], program_arguments[2])
            return

        summary = parse_args_and_process_files(filter(lambda a: a != '-o', program_arguments))

        print(summary)
        if '-o' in program_arguments:
            write_to_otuput_dir(summary)


if __name__ == '__main__':
    main()
