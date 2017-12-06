#!/usr/bin/env python3
import sys
import os

from collections import defaultdict
from typing import List

from dump_file import parse_dump_file
from rules import NormalRule, process_custom

ENSURE_PARSED = "LazyParseableElement.getFirstChildNode"

FRAME_SEQ_TO_TICKET = [
    NormalRule(["com.intellij.find.findUsages.PsiElement2UsageTargetAdapter.isValid", ENSURE_PARSED],
               "usages view https://youtrack.jetbrains.com/issue/CPP-8459"),
    NormalRule(["com.intellij.usages.UsageInfo2UsageAdapter.isValid", ENSURE_PARSED],
               "usages view https://youtrack.jetbrains.com/issue/CPP-8459"),
    NormalRule(["com.intellij.usages.impl.UsageViewImpl.checkNodeValidity", ENSURE_PARSED],
               "usages view https://youtrack.jetbrains.com/issue/CPP-8459"),

    NormalRule(
        ["com.intellij.codeInsight.highlighting.BraceHighlightingHandler.lookForInjectedAndMatchBracesInOtherThread",
         ENSURE_PARSED],
        "brace matcher (https://youtrack.jetbrains.com/issue/IDEA-177314)"),

    NormalRule(
        ["com.intellij.codeInsight.highlighting.BraceHighlightingHandler.lookForInjectedAndMatchBracesInOtherThread",
         ENSURE_PARSED],
        "brace matcher (https://youtrack.jetbrains.com/issue/IDEA-177314)"),

    NormalRule(["com.intellij.codeInsight.folding.impl.CodeFoldingManagerImpl.writeFoldingState", ENSURE_PARSED],
               "Save folding state (https://youtrack.jetbrains.com/issue/CPP-10639)"),
    NormalRule(["com.intellij.codeInsight.folding.impl.CodeFoldingManagerImpl.saveFoldingState", ENSURE_PARSED],
               "Save folding state (https://youtrack.jetbrains.com/issue/CPP-10639)"),
    NormalRule(["com.intellij.configurationStore.ComponentStoreImpl.save",
                "TextEditorState.getFoldingState",
                ENSURE_PARSED],
               "Save folding state (https://youtrack.jetbrains.com/issue/CPP-10639)"),

    NormalRule(["com.intellij.codeInsight.highlighting.HighlightUsagesHandlerFactoryBase.createHighlightUsagesHandler",
                ENSURE_PARSED],
               "create IdentifierHighlighterPass pass (https://youtrack.jetbrains.com/issue/CPP-9373)"),

    NormalRule(["com.jetbrains.cidr.lang.navigation.OCGotoDeclarationHandler.getActionText"],
               "goto declaration action text https://youtrack.jetbrains.com/issue/CPP-8460"),

    NormalRule(["com.jetbrains.cidr.lang.editor.parameterInfo.OCArgumentListCallPlace.collectCallOptions"],
               "parameter info https://youtrack.jetbrains.com/issue/CPP-9361"),

    NormalRule(["com.jetbrains.cidr.lang.editor.OCFunctionParameterInfoHandler.updateParameterInfo"],
               "parameter info https://youtrack.jetbrains.com/issue/CPP-9361"),

    NormalRule(["com.jetbrains.cidr.lang.navigation.OCSwitchToHeaderOrSourceRelatedProvider.getItems"],
               "switch to source/header https://youtrack.jetbrains.com/issue/CPP-7168"),

    NormalRule(["com.jetbrains.cidr.lang.quickfixes.OCImportSymbolFix.showHint",
                "com.jetbrains.cidr.lang.symbols.cpp.OCStructSymbol.getKindUppercase"],
               "Import symbol fix https://youtrack.jetbrains.com/issue/CPP-10663"),

    NormalRule(["com.jetbrains.cidr.projectView.CidrFilesViewHelper$2.customizeCellRenderer",
                "com.jetbrains.cidr.lang.search.scopes.OCSearchScope.getExplicitlySpecifiedProjectSourceFiles"],
               "drawing project tree https://youtrack.jetbrains.com/issue/CPP-10691"),

    NormalRule(["com.jetbrains.cidr.lang.refactoring.changeSignature.OCChangeSignatureProcessor.runSynchronously",
                "com.jetbrains.cidr.lang.refactoring.changeSignature.OCChangeSignatureUsageProcessor.findConflicts"],
               "Change signature: find conflicts"),

    NormalRule(["com.jetbrains.cidr.lang.refactoring.changeSignature.OCChangeSignatureProcessor.preprocessUsages"],
               "Change signature: preprocessUsages"),

    NormalRule(["com.intellij.ide.actions.SearchEverywhereAction",
                "com.jetbrains.cidr.lang.symbols.OCSymbolBase.canNavigate",
                ENSURE_PARSED],
               "Search everywhere -> canNavigate -> reparsing"),

    NormalRule(["com.intellij.openapi.progress.util.PotemkinProgress.runInSwingThread"],
               "Potemkin progress"),

    NormalRule(["com.intellij.ide.util.treeView.AbstractTreeStructureBase.getChildElements",
                "com.jetbrains.cidr.lang.OCHeaderFileTypeDetector.detect"],
               "Project view: file type detector"),

    NormalRule(["com.intellij.execution.filters.FileHyperlinkInfoBase.navigate",
                ENSURE_PARSED],
               "File hyper links: reparse"),

    NormalRule(["com.intellij.find.actions.FindInPathAction.actionPerformed",
                "com.intellij.find.impl.FindInProjectUtil.setDirectoryName",
                "com.jetbrains.cidr.lang.symbols.OCSymbolBase.locateDefinition",
                ENSURE_PARSED],
               "Find in path: reparse"),

    NormalRule(["com.jetbrains.cidr.lang.formatting.OCAutoFormatTypedHandler.execute",
                "com.intellij.psi.util.PsiUtilBase.getLanguageInEditor",
                ENSURE_PARSED],
               "Auto format typed handler: get language and reparse"),

    NormalRule(["com.jetbrains.cidr.lang.symbols.symtable.FileSymbolTablesCache$3.after",
                "com.intellij.util.indexing.FileBasedIndexImpl$ChangedFilesCollector.ensureUpToDateAsync"],
               "File symbols cache: ensure up-to-date async"),

    NormalRule(["com.jetbrains.cidr.generate.actions.OCBaseGenerateTestAction.update",
                "com.jetbrains.cidr.generate.actions.OCBaseGenerateTestAction.isValidForFile"],
               "Generate test: is valid for"),

    NormalRule(["com.jetbrains.cidr.lang.refactoring.inline.OCInlineActionHandlerBase.inlineElement"], "Inline"),

    NormalRule(["com.jetbrains.cidr.lang.refactoring.OCExtractMethodHandler.invoke",
                "com.jetbrains.cidr.lang.refactoring.OCExtractMethodProcessor.invoke"],
               "Extract method"),

    NormalRule(["com.jetbrains.cidr.lang.symbols.cpp.OCSymbolWithQualifiedName.processSameSymbols",
                "com.jetbrains.cidr.lang.refactoring.move.ui.OCAbstractMoveDialog.setMembersChecked"],
               "Move"),

    NormalRule(["com.jetbrains.cidr.lang.refactoring.move.handlers.OCMoveTopLevelRefactoringHandler.showDialog",
                "com.jetbrains.cidr.lang.refactoring.move.OCDependentMembersCollector.collect"],
               "Move"),

    NormalRule(["com.jetbrains.cidr.lang.refactoring.move.OCMoveProcessor"],
               "Move"),

    NormalRule(["OCMoveRefactoringHandler.showDialog"],
               "Move"),

    NormalRule(["com.intellij.codeInsight.editorActions.EnterHandler"],
               "Enter handler"),

    NormalRule(["com.intellij.openapi.actionSystem.impl.Utils.fillMenu",
                "com.jetbrains.cidr.execution.testing.CidrTestRunConfigurationProducer.isConfigurationFromContext"],
               "Context configuration click"),

    NormalRule(["com.jetbrains.cidr.execution.CidrRunConfigurationSettingsEditor$MyComboBox.fireSelectedItemChanged",
                "com.jetbrains.cidr.execution.testing.google.CidrGoogleTestRunConfigurationData"],
               "Google test run configuration editor"),

    NormalRule(["com.jetbrains.cidr.lang.symbols.cpp.OCSymbolWithQualifiedName.getLocationString"],
               "getLocationString() (https://youtrack.jetbrains.com/issue/CPP-10102)"),

    NormalRule(
        ["FileSymbolTablesCache$OCCodeBlockModificationListener.treeChanged",
         ENSURE_PARSED],
        "lazy reparsing (in processASTNodeForMacros?)"),

    NormalRule(["OCTypedHandlerDelegate.charTyped",
                "PsiDocumentManagerBase.commitDocument"],
               "commit on typing https://youtrack.jetbrains.com/issue/CPP-11365"),

    NormalRule(["TextEditorPsiDataProvider.getData",
                "TargetElementUtil.findTargetElement"],
               "getData(PSI_ELEMENT)"),

    NormalRule(["com.intellij.ide.actions.NextOccurenceAction.go",
                ENSURE_PARSED],
               "next occurence -> reparsing"),

    NormalRule(["com.intellij.openapi.editor.impl.EditorGutterComponentImpl",
                "com.jetbrains.cidr.lang.navigation.OCGotoAction.navigate"],
               "gutter -> goto"),

    NormalRule(["com.jetbrains.cidr.execution.debugger.breakpoints.CidrWatchpointHandler.cleanup"],
               "WA in stop breakpoint (https://youtrack.jetbrains.com/issue/CPP-11330)"),

    NormalRule(["com.intellij.injected.editor.DocumentWindowImpl.isValid",
                "com.intellij.psi.impl.source.tree.injected.ShredImpl.isValid",
                ENSURE_PARSED],
               "DocumentWindowImpl.isValid -> reparse"),

    NormalRule(["MyAutoScrollFromSourceHandler",
                "SelectInTargetPsiWrapper.selectIn",
                ENSURE_PARSED],
               "Autoscroll to source -> reparse"),

    NormalRule(["OCCppDefinitionsUtil.getOutsidePreferredPosition", "OCSplitFunctionIntentionAction.invoke"],
               "Split function (https://youtrack.jetbrains.com/issue/CPP-11254)"),

    NormalRule(["OCGenerateUtil.applyReplacements", "OCImportSymbolFix.fixAllSymbolsRecursively"],
               "Generate definition: import fix"),

    NormalRule(["OCRenameProcessor.prepareRenaming"],
               "Rename"),

    NormalRule(["OCInplaceRenameHandler.doRename"],
               "Rename"),

    NormalRule(["OCCreateNewDefinitionIntentionAction.getText"],
               "OCCreateNewDefinitionIntentionAction.getText"),

    NormalRule(["OCCCppGenerateHandlerBase.invoke"],
               "CPP generate action"),

    NormalRule(["GotoDeclarationAction.update", ENSURE_PARSED],
               "Goto declaration -> reparse"),

    NormalRule(["SelectWordHandler.doExecute", ENSURE_PARSED],
               "Select word/expand selection -> reparse"),

    NormalRule(["CodeFoldingManagerImpl$1.mouseMoved", ENSURE_PARSED],
               "Folding + mouse moved -> reparse"),

    NormalRule(["TextEditorPsiDataProvider.getData", ENSURE_PARSED],
               "TextEditorPsiDataProvider -> reparse"),

    NormalRule(["CidrTestWithScopeElementsFramework.getTestLinks"],
               "CidrTestWithScopeElementsFramework.getTestLinks"),

    # If a typical thread dump for a freeze has several characteristic frames in EDT,
    # add the following entry:
    # NormalRule(["frame.substring.1", "frame.substring.2", <...>], "ticket URL and description")
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
                if not l.strip():
                    break

    return res


def match_stack(stack):
    if stack is not None:
        custom = process_custom(stack)
        if custom is not None:
            return {custom}
        messages = set()
        for rule in FRAME_SEQ_TO_TICKET:
            message = rule.is_matched(stack)
            if message:
                messages.add(message)
        return messages
    else:
        return set()


class ThreadDumpInfo:
    def __init__(self, file_name, messages, lines):
        self.file_name = file_name
        self.messages = messages
        self.lines = lines


def process_thread_dump(file_name, lines: List[str]):
    stack = extract_edt_call_stack(lines)
    dump_info = parse_dump_file(lines)
    messages = match_stack(dump_info)
    return ThreadDumpInfo(file_name, messages, stack)


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

    return "All found tickets:\n{}\nUnknown traces ({}):\n{}\n\n{}".format(
        tickets_to_string(all_tickets),
        len(unknown),
        "\n".join(unknown),
        "".join(detailed))


def tickets_to_string(all_tickets):
    return "\n".join(
        "   {}: {}".format(t, u) for t, u in sorted(all_tickets.items(), key=lambda k: (k[1], k[0]), reverse=True))


def collect_files(arg):
    if os.path.isfile(arg):
        yield arg
    elif os.path.isdir(arg):
        for folder_name, subfolders, filenames in os.walk(arg):
            if ".git" in folder_name:
                continue

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
