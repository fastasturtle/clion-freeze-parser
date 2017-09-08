#!/usr/bin/env python3
import sys
import os

KNOWN_FRAMES = [
    ("com.intellij.find.findUsages.PsiElement2UsageTargetAdapter.isValid",
     "https://youtrack.jetbrains.com/issue/CPP-8459"),
    ("com.jetbrains.cidr.lang.navigation.OCGotoDeclarationHandler.getActionText",
     "https://youtrack.jetbrains.com/issue/CPP-8460")
]


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


def find_tickets(stack):
    decorated_lines = []
    ticket_ids = set()
    for l in stack:
        for substr, id in KNOWN_FRAMES:
            if substr in l:
                decorated_lines.append('*' + l)
                ticket_ids.add(id)
            else:
                decorated_lines.append(l)

    return decorated_lines, ticket_ids


def process_thread_dump(lines):
    stack = extract_edt_call_stack(lines)
    has_cidr = any(".cidr" in l for l in lines)
    decorated_lines, ticket_ids = find_tickets(stack)
    return "CIDR?: {}, tickets: {}\n\n{}".format(
        has_cidr,
        ", ".join(ticket_ids),
        "".join(decorated_lines))


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
