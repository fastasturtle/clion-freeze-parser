#!/usr/bin/env python3
import sys
import os
import glob

FRAME_SEQ_TO_TICKET = [
    (("com.intellij.find.findUsages.PsiElement2UsageTargetAdapter.isValid",
      "com.jetbrains.cidr.lang.parser.OCFileElementType.parseContents"),
     "https://youtrack.jetbrains.com/issue/CPP-8459"),

    (("com.intellij.codeInsight.highlighting.BraceHighlightingHandler.lookForInjectedAndMatchBracesInOtherThread",
      "com.jetbrains.cidr.lang.parser.OCFileElementType.parseContents"),
     "https://youtrack.jetbrains.com/issue/IDEA-177314"),

    (("com.intellij.codeInsight.folding.impl.CodeFoldingManagerImpl.writeFoldingState",
      "com.jetbrains.cidr.lang.parser.OCFileElementType.parseContents"),
     "https://youtrack.jetbrains.com/issue/CPP-10639"),

    (("com.intellij.codeInsight.folding.impl.CodeFoldingManagerImpl.saveFoldingState",
      "com.jetbrains.cidr.lang.parser.OCFileElementType.parseContents"),
     "https://youtrack.jetbrains.com/issue/CPP-10639"),

    (("com.intellij.codeInsight.highlighting.HighlightUsagesHandlerFactoryBase.createHighlightUsagesHandler",
      "com.jetbrains.cidr.lang.parser.OCFileElementType.parseContents"),
     "https://youtrack.jetbrains.com/issue/CPP-9373"),

    (("com.jetbrains.cidr.lang.navigation.OCGotoDeclarationHandler.getActionText",),
     "https://youtrack.jetbrains.com/issue/CPP-8460"),

    (("com.jetbrains.cidr.lang.editor.parameterInfo.OCArgumentListCallPlace.collectCallOptions",),
     "https://youtrack.jetbrains.com/issue/CPP-9361"),

    (("com.jetbrains.cidr.lang.editor.OCFunctionParameterInfoHandler.updateParameterInfo",),
     "https://youtrack.jetbrains.com/issue/CPP-9361"),

    (("com.jetbrains.cidr.lang.navigation.OCSwitchToHeaderOrSourceRelatedProvider.getItems",),
     "https://youtrack.jetbrains.com/issue/CPP-7168"),

    (("com.jetbrains.cidr.lang.quickfixes.OCImportSymbolFix.showHint",
      "com.jetbrains.cidr.lang.symbols.cpp.OCStructSymbol.getKindUppercase"),
     "https://youtrack.jetbrains.com/issue/CPP-10663"),

    # If a typical thread dump for a freeze has several characteristic frames in EDT,
    # add the following entry:
    # ("frame.substring.1", "frame.substring.2", <...>), "ticket URL")
]

KNOWN_FRAMES = set([frame for frames, _ in FRAME_SEQ_TO_TICKET for frame in frames])


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
                if not l.strip():
                    break

    return res


def find_tickets(stack):
    ticket_ids = set()
    known_frames = set()
    for l in stack:
        for frame in KNOWN_FRAMES:
            if frame in l:
                known_frames.add(frame)

    for frame_seq, ticket_id in FRAME_SEQ_TO_TICKET:
        match = True
        for frame in frame_seq:
            if frame not in known_frames:
                match = False
                break
        if match:
            ticket_ids.add(ticket_id)

    return stack, ticket_ids


class ThreadDumpInfo:
    def __init__(self, file_name, ticket_ids, lines):
        self.file_name = file_name
        self.ticket_ids = ticket_ids
        self.lines = lines


def process_thread_dump(file_name, lines):
    stack = extract_edt_call_stack(lines)
    lines, ticket_ids = find_tickets(stack)
    return ThreadDumpInfo(file_name, ticket_ids, lines)


def process_file(file_name):
    with open(file_name) as f:
        try:
            readlines = f.readlines()
        except (IOError, UnicodeError):
            readlines = []  # will be reported as "UNKNOWN"
        return process_thread_dump(file_name, readlines)


def get_summary(infos):
    all_tickets = set()
    detailed = []
    unknown = []
    for info in infos:
        if not info.ticket_ids:
            unknown.append(info.file_name)
        detailed.append(
            info.file_name + ": " + (", ".join(info.ticket_ids) if info.ticket_ids else "UNKNOWN") +
            "\n" +
            ("" if info.ticket_ids else ("\n" + "".join(info.lines)))
        )
        all_tickets.update(info.ticket_ids)

    return "All found tickets: " + ", ".join(all_tickets) + "\n" + \
           "Unknown traces:\n" + "\n".join(unknown) + "\n\n" + \
           "".join(detailed)


def process_files(pattern_or_file_or_dir):
    pattern = pattern_or_file_or_dir + "/**/*.txt" if os.path.isdir(pattern_or_file_or_dir) else pattern_or_file_or_dir
    return get_summary(
        process_file(f)
        for f in glob.iglob(pattern, recursive=True)
        if not os.path.isdir(f))


def main():
    if len(sys.argv) < 2:
        print_usage()

    for arg in sys.argv[1:]:
        print(process_files(arg))


if __name__ == '__main__':
    main()
