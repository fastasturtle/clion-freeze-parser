#!/usr/bin/env python3
import sys
import os

from collections import defaultdict

FRAME_SEQ_TO_TICKET = [
    (("com.intellij.find.findUsages.PsiElement2UsageTargetAdapter.isValid",
      "com.jetbrains.cidr.lang.parser.OCFileElementType.parseContents"),
     "chameleon in findUsages view https://youtrack.jetbrains.com/issue/CPP-8459"),
    (("com.intellij.usages.UsageInfo2UsageAdapter.isValid",
      "com.jetbrains.cidr.lang.parser.OCFileElementType.parseContents"),
     "chameleon in findUsages view https://youtrack.jetbrains.com/issue/CPP-8459"),
    (("com.intellij.usages.impl.UsageViewImpl.checkNodeValidity",
      "com.jetbrains.cidr.lang.parser.OCFileElementType.parseContents"),
     "chameleon in findUsages view https://youtrack.jetbrains.com/issue/CPP-8459"),

    (("com.intellij.find.findUsages.PsiElement2UsageTargetAdapter.isValid",
      "com.jetbrains.cidr.lang.parser.OCFileElementType.parseContents"),
     "https://youtrack.jetbrains.com/issue/CPP-8459"),

    (("com.intellij.codeInsight.highlighting.BraceHighlightingHandler.lookForInjectedAndMatchBracesInOtherThread",
      "com.jetbrains.cidr.lang.parser.OCFileElementType.parseContents"),
     "fixed https://youtrack.jetbrains.com/issue/IDEA-177314"),

    (("com.intellij.codeInsight.highlighting.BraceHighlightingHandler.lookForInjectedAndMatchBracesInOtherThread",
      "com.jetbrains.cidr.lang.parser.OCReparseablePsiElementType.doParseContents"),
     "fixed https://youtrack.jetbrains.com/issue/IDEA-177314"),

    (("com.intellij.codeInsight.folding.impl.CodeFoldingManagerImpl.writeFoldingState",
      "com.jetbrains.cidr.lang.parser.OCReparseablePsiElementType.doParseContents"),
     "folding+lazy block https://youtrack.jetbrains.com/issue/CPP-10639"),

    (("com.intellij.codeInsight.folding.impl.CodeFoldingManagerImpl.writeFoldingState",
      "com.jetbrains.cidr.lang.parser.OCFileElementType.parseContents"),
     "fixed? https://youtrack.jetbrains.com/issue/CPP-10639"),

    (("com.intellij.codeInsight.folding.impl.CodeFoldingManagerImpl.saveFoldingState",
      "com.jetbrains.cidr.lang.parser.OCFileElementType.parseContents"),
     "fixed? https://youtrack.jetbrains.com/issue/CPP-10639"),

    (("com.intellij.configurationStore.ComponentStoreImpl.save",
      "com.intellij.openapi.fileEditor.impl.text.TextEditorState.getFoldingState",
      "com.jetbrains.cidr.lang.parser.OCFileElementType.parseContents"),
     "fixed? https://youtrack.jetbrains.com/issue/CPP-10639"),

    (("com.intellij.codeInsight.highlighting.HighlightUsagesHandlerFactoryBase.createHighlightUsagesHandler",
      "com.jetbrains.cidr.lang.parser.OCFileElementType.parseContents"),
     "https://youtrack.jetbrains.com/issue/CPP-9373"),

    (("com.jetbrains.cidr.lang.navigation.OCGotoDeclarationHandler.getActionText",),
     "fixed https://youtrack.jetbrains.com/issue/CPP-8460"),

    (("com.jetbrains.cidr.lang.editor.parameterInfo.OCArgumentListCallPlace.collectCallOptions",),
     "https://youtrack.jetbrains.com/issue/CPP-9361"),

    (("com.jetbrains.cidr.lang.editor.OCFunctionParameterInfoHandler.updateParameterInfo",),
     "https://youtrack.jetbrains.com/issue/CPP-9361"),

    (("com.jetbrains.cidr.lang.navigation.OCSwitchToHeaderOrSourceRelatedProvider.getItems",),
     "https://youtrack.jetbrains.com/issue/CPP-7168"),

    (("com.jetbrains.cidr.lang.quickfixes.OCImportSymbolFix.showHint",
      "com.jetbrains.cidr.lang.symbols.cpp.OCStructSymbol.getKindUppercase"),
     "https://youtrack.jetbrains.com/issue/CPP-10663"),

    (("com.jetbrains.cidr.projectView.CidrFilesViewHelper$2.customizeCellRenderer",
      "com.jetbrains.cidr.lang.search.scopes.OCSearchScope.getExplicitlySpecifiedProjectSourceFiles"),
     "https://youtrack.jetbrains.com/issue/CPP-10691"),

    (("sun.misc.Unsafe.park(Native Method)",),
     "unknown (waiting)"),

    (("com.intellij.openapi.progress.util.AbstractProgressIndicatorExBase.checkCanceled(AbstractProgressIndicatorExBase.java:102)",),
     "unknown (progress indicator)"),

    (("com.jetbrains.cidr.lang.refactoring.changeSignature.OCChangeSignatureProcessor.runSynchronously",
      "com.jetbrains.cidr.lang.refactoring.changeSignature.OCChangeSignatureUsageProcessor.findConflicts"),
     "Change signature: find conflicts"),

    (("com.jetbrains.cidr.lang.refactoring.changeSignature.OCChangeSignatureProcessor.preprocessUsages",),
     "Change signature: preprocessUsages"),

    (("com.intellij.ide.actions.SearchEverywhereAction",
      "com.jetbrains.cidr.lang.symbols.OCSymbolBase.canNavigate",
      "com.jetbrains.cidr.lang.parser.OCFileElementType.parseContents"),
     "Search everywhere -> canNavigate -> reparsing"),

    (("com.intellij.openapi.progress.util.PotemkinProgress.runInSwingThread",),
     "Potemkin progress not working"),

    (("sun.java2d.opengl.OGLRenderQueue$QueueFlusher.flushNow",
      "java.lang.Object.wait"),
     "OpenGL wait"),

    (("com.intellij.history.integration.IdeaGateway.areContentChangesVersioned",
      "com.intellij.history.integration.LocalHistoryEventDispatcher."),
     "local history: areContentChangesVersioned"),

    (("com.intellij.ide.util.treeView.AbstractTreeStructureBase.getChildElements",
      "com.jetbrains.cidr.lang.OCHeaderFileTypeDetector.detect"),
     "Project view: file type detector"),

    (("com.jetbrains.cidr.lang.symbols.symtable.FileSymbolTablesCache$OCCodeBlockModificationListener.treeChanged",
      "com.intellij.openapi.fileEditor.impl.LoadTextUtil.loadText"),
     "File symbol cache: load text"),

    (("com.intellij.execution.filters.FileHyperlinkInfoBase.navigate",
      "com.jetbrains.cidr.lang.parser.OCFileElementType.parseContents"),
     "File hyper links: reparse"),

    (("com.intellij.find.actions.FindInPathAction.actionPerformed",
      "com.intellij.find.impl.FindInProjectUtil.setDirectoryName",
      "com.jetbrains.cidr.lang.symbols.OCSymbolBase.locateDefinition",
      "com.jetbrains.cidr.lang.parser.OCFileElementType.parseContents"),
     "Find in path: reparse"),

    (("com.jetbrains.cidr.lang.formatting.OCAutoFormatTypedHandler.execute",
      "com.intellij.psi.util.PsiUtilBase.getLanguageInEditor",
      "com.jetbrains.cidr.lang.parser.OCFileElementType.parseContents"),
     "Auto format typed handler: get language and reparse"),

    (("com.jetbrains.cidr.lang.symbols.symtable.FileSymbolTablesCache$3.after",
      "com.intellij.util.indexing.FileBasedIndexImpl$ChangedFilesCollector.ensureUpToDateAsync"),
     "File symbols cache: ensure up-to-date async"),

    (("com.jetbrains.cidr.generate.actions.OCBaseGenerateTestAction.update",
      "com.jetbrains.cidr.generate.actions.OCBaseGenerateTestAction.isValidForFile"),
     "Generate test: is valid for"),

    (("com.jetbrains.cidr.lang.refactoring.inline.OCInlineActionHandlerBase.inlineElement",
      "com.jetbrains.cidr.lang.refactoring.inline.OCInlineActionHandlerBase.findUsages"),
     "Inline element: findUsages"),

    (("com.jetbrains.cidr.lang.refactoring.OCExtractMethodHandler.invoke",
      "com.jetbrains.cidr.lang.refactoring.OCExtractMethodProcessor.invoke"),
     "Extract method"),

    (("com.jetbrains.cidr.lang.symbols.cpp.OCSymbolWithQualifiedName.processSameSymbols",
      "com.jetbrains.cidr.lang.refactoring.move.ui.OCAbstractMoveDialog.setMembersChecked"),
     "Move"),

    (("com.jetbrains.cidr.lang.refactoring.move.handlers.OCMoveTopLevelRefactoringHandler.showDialog",
      "com.jetbrains.cidr.lang.refactoring.move.OCDependentMembersCollector.collect"),
     "Move"),

    (("com.jetbrains.cidr.lang.refactoring.move.OCMoveProcessor",),
     "Move"),

    (("com.intellij.codeInsight.editorActions.EnterHandler",),
     "Enter handler"),

    (("com.intellij.openapi.actionSystem.impl.Utils.fillMenu",
      "com.jetbrains.cidr.execution.testing.CidrTestRunConfigurationProducer.isConfigurationFromContext"),
     "Context configuration click"),

    (("com.jetbrains.cidr.execution.CidrRunConfigurationSettingsEditor$MyComboBox.fireSelectedItemChanged",
      "com.jetbrains.cidr.execution.testing.google.CidrGoogleTestRunConfigurationData"),
     "Google test run configuration editor"),

    (("com.jetbrains.cidr.lang.symbols.cpp.OCSymbolWithQualifiedName.getLocationString",),
     "getLocationString() (https://youtrack.jetbrains.com/issue/CPP-10102)"),

    (("com.intellij.util.ProfilingUtil",),
     "reporting activity"),
    (("com.intellij.ide.actions.CollectZippedLogsAction",),
     "reporting activity"),

    (("com.jetbrains.cidr.lang.symbols.symtable.FileSymbolTablesCache$OCCodeBlockModificationListener.treeChanged",
      "com.intellij.psi.impl.source.tree.LazyParseableElement.ensureParsed"),
     "lazy reparsing (in processASTNodeForMacros?)"),

    (("OCTypedHandlerDelegate.charTyped",
      "PsiDocumentManagerBase.commitDocument"),
     "lazy reparsing (in processASTNodeForMacros?)"),

    (("TextEditorPsiDataProvider.getData",
      "TargetElementUtil.findTargetElement"),
     "getData(PSI_ELEMENT)"),

    (("com.intellij.ide.actions.NextOccurenceAction.go",
      "com.intellij.psi.impl.source.tree.LazyParseableElement.ensureParsed"),
     "lazy reparsing (next occurence)"),

    (("com.intellij.openapi.editor.impl.EditorGutterComponentImpl",
      "com.jetbrains.cidr.lang.navigation.OCGotoAction.navigate"),
     "gutter -> goto")

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
    all_tickets = defaultdict(int)
    detailed = []
    unknown = []
    for info in infos:
        if not info.ticket_ids:
            unknown.append(info.file_name)
        detailed.append(
            info.file_name + ": " + (", ".join(info.ticket_ids) if info.ticket_ids else "UNKNOWN") +
            "\n" +
            ("" if info.ticket_ids else ("\n" + "".join(info.lines) + "\n"))
        )
        for t in info.ticket_ids:
            all_tickets[t] += 1

    return "All found tickets:\n{}\nUnknown traces ({}):\n{}\n\n{}".format(
        tickets_to_string(all_tickets),
        len(unknown),
        "\n".join(unknown),
        "".join(detailed))


def tickets_to_string(all_tickets):
    return "\n".join("   {}: {}".format(t, u) for t, u in sorted(all_tickets.items(), key=lambda k: k[1], reverse=True))


def collect_files(arg):
    if os.path.isfile(arg):
        yield arg
    elif os.path.isdir(arg):
        for folder_name, subfolders, filenames in os.walk(arg):
            if filenames and 'threadDumps-freeze-20' in folder_name:
                # assume all freezes in this folder have the same cause
                yield folder_name + '/' + filenames[0]
            else:
                for file in filenames:
                    yield folder_name + '/' + file
    else:
        raise ValueError("Invalid file or folder: " + str(arg))


def parse_args_and_process_files(args):
    files = [f for arg in args for f in collect_files(arg)]
    return get_summary(process_file(f) for f in files)


def main():
    if len(sys.argv) < 2:
        print_usage()
    else:
        print(parse_args_and_process_files(sys.argv[1:]))


if __name__ == '__main__':
    main()
