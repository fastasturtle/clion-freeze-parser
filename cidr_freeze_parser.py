#!/usr/bin/env python3

import sys
import os


def print_usage():
    print("Usage: {} [thread dumps file]".format(os.path.basename(__file__)))


def extract_edt_call_stack(lines):
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
                break

    return res


def process_thread_dump(lines):
    stack = extract_edt_call_stack(lines)
    has_cidr = any(".cidr" in l for l in lines)
    return "CIDR related: {}\n\n".format(has_cidr) + "".join(stack)


def process_file(fileName):
    with open(fileName) as f:
        print(process_thread_dump(f.readlines()))


def main():
    if len(sys.argv) < 2:
        print_usage()

    for arg in sys.argv[1:]:
        print(process_file(arg))


if __name__ == '__main__':
    main()
