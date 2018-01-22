from rules import NormalRule
ENSURE_PARSED = "LazyParseableElement.getFirstChildNode"


def get_rules():
    rules = [
        NormalRule(["com.intellij.find.findUsages.PsiElement2UsageTargetAdapter.isValid", ENSURE_PARSED],
                   "usages view https://youtrack.jetbrains.com/issue/CPP-8459"),
        NormalRule(["com.intellij.usages.UsageInfo2UsageAdapter.isValid", ENSURE_PARSED],
                   "usages view https://youtrack.jetbrains.com/issue/CPP-8459"),
        NormalRule(["com.intellij.usages.impl.UsageViewImpl.checkNodeValidity", ENSURE_PARSED],
                   "usages view https://youtrack.jetbrains.com/issue/CPP-8459"),

        NormalRule(["BraceHighlightingHandler.lookForInjectedAndMatchBracesInOtherThread", ENSURE_PARSED],
                   "brace matcher (https://youtrack.jetbrains.com/issue/IDEA-177314)"),

        NormalRule(["com.intellij.configurationStore.ComponentStoreImpl.save",
                    "TextEditorState.getFoldingState", ENSURE_PARSED],
                   "Save folding state (https://youtrack.jetbrains.com/issue/CPP-10639)"),
        NormalRule(["com.intellij.codeInsight.folding.impl.CodeFoldingManagerImpl.writeFoldingState", ENSURE_PARSED],
                   "Save folding state (https://youtrack.jetbrains.com/issue/CPP-10639)"),
        NormalRule(["com.intellij.codeInsight.folding.impl.CodeFoldingManagerImpl.saveFoldingState", ENSURE_PARSED],
                   "Save folding state (https://youtrack.jetbrains.com/issue/CPP-10639)"),

        NormalRule(["HighlightUsagesHandlerFactoryBase.createHighlightUsagesHandler", ENSURE_PARSED],
                   "create IdentifierHighlighterPass pass (https://youtrack.jetbrains.com/issue/CPP-9373)"),

        NormalRule(["com.intellij.ide.actions.SearchEverywhereAction",
                    "com.jetbrains.cidr.lang.symbols.OCSymbolBase.canNavigate",
                    ENSURE_PARSED],
                   "Search everywhere -> canNavigate -> reparse"),

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

        NormalRule(["FileSymbolTablesCache$OCCodeBlockModificationListener.treeChanged", ENSURE_PARSED],
                   "FileSymbolTablesCache$OCCodeBlockModificationListener.treeChanged"),

        NormalRule(["com.intellij.ide.actions.NextOccurenceAction.go", ENSURE_PARSED],
                   "next occurence -> reparse"),

        NormalRule(["com.intellij.injected.editor.DocumentWindowImpl.isValid",
                    "com.intellij.psi.impl.source.tree.injected.ShredImpl.isValid",
                    ENSURE_PARSED],
                   "DocumentWindowImpl.isValid -> reparse"),

        NormalRule(["MyAutoScrollFromSourceHandler", "SelectInTargetPsiWrapper.selectIn", ENSURE_PARSED],
                   "Autoscroll to source -> reparse"),

        NormalRule(["GotoDeclarationAction.update", ENSURE_PARSED],
                   "Goto declaration update -> reparse"),

        NormalRule(["SelectWordHandler.doExecute", ENSURE_PARSED],
                   "Select word/expand selection -> reparse"),

        NormalRule(["CodeFoldingManagerImpl$1.mouseMoved", ENSURE_PARSED],
                   "Folding + mouse moved -> reparse"),

        NormalRule(["TextEditorPsiDataProvider.getData", ENSURE_PARSED],
                   "TextEditorPsiDataProvider -> reparse"),
    ]
    return rules
