#!/usr/bin/env python3
import sys
import os

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
    decorated_lines = []
    ticket_ids = set()
    known_frames = set()
    for l in stack:
        known = False
        for frame in KNOWN_FRAMES:
            if frame in l:
                known = True
                known_frames.add(frame)
        decorated_lines.append(('*' if known else '') + l)

    for frame_seq, ticket_id in FRAME_SEQ_TO_TICKET:
        match = True
        for frame in frame_seq:
            if frame not in known_frames:
                match = False
                break
        if match:
            ticket_ids.add(ticket_id)

    return decorated_lines, ticket_ids


def process_thread_dump(lines):
    stack = extract_edt_call_stack(lines)
    has_cidr = any(".cidr" in l for l in lines)
    decorated_lines, ticket_ids = find_tickets(stack)
    return "CIDR?: {}, tickets: {}\n\n{}".format(
        has_cidr,
        ", ".join(ticket_ids),
        "".join(decorated_lines))


def process_file(file_name):
    res = []
    with open(file_name) as f:
        res.append(process_thread_dump(f.readlines()))
    return "\n".join(res)


def main():
    if len(sys.argv) < 2:
        print_usage()

    for arg in sys.argv[1:]:
        print(process_file(arg))


if __name__ == '__main__':
    main()
