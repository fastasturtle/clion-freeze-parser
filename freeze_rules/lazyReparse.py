from rules import NormalRule
ENSURE_PARSED = "LazyParseableElement.getFirstChildNode"


def get_rules():
    rules = [
        NormalRule(["PsiElement2UsageTargetAdapter.isValid", ENSURE_PARSED],
                   "usages view https://youtrack.jetbrains.com/issue/CPP-8459"),
        NormalRule(["UsageInfo2UsageAdapter.isValid", ENSURE_PARSED],
                   "usages view https://youtrack.jetbrains.com/issue/CPP-8459"),
        NormalRule(["UsageViewImpl.checkNodeValidity", ENSURE_PARSED],
                   "usages view https://youtrack.jetbrains.com/issue/CPP-8459"),

        NormalRule(["BraceHighlightingHandler.lookForInjectedAndMatchBracesInOtherThread", ENSURE_PARSED],
                   "brace matcher (https://youtrack.jetbrains.com/issue/IDEA-177314)"),

        NormalRule(["ComponentStoreImpl.save",
                    "TextEditorState.getFoldingState", ENSURE_PARSED],
                   "Save folding state (https://youtrack.jetbrains.com/issue/CPP-10639)"),
        NormalRule(["CodeFoldingManagerImpl.writeFoldingState", ENSURE_PARSED],
                   "Save folding state (https://youtrack.jetbrains.com/issue/CPP-10639)"),
        NormalRule(["CodeFoldingManagerImpl.saveFoldingState", ENSURE_PARSED],
                   "Save folding state (https://youtrack.jetbrains.com/issue/CPP-10639)"),

        NormalRule(["HighlightUsagesHandlerFactoryBase.createHighlightUsagesHandler", ENSURE_PARSED],
                   "create IdentifierHighlighterPass pass (https://youtrack.jetbrains.com/issue/CPP-9373)"),

        NormalRule(["SearchEverywhereAction",
                    "OCSymbolBase.canNavigate",
                    ENSURE_PARSED],
                   "Search everywhere -> canNavigate -> reparse"),

        NormalRule(["FileHyperlinkInfoBase.navigate",
                    ENSURE_PARSED],
                   "File hyper links: reparse"),

        NormalRule(["FindInPathAction.actionPerformed",
                    "FindInProjectUtil.setDirectoryName",
                    "OCSymbolBase.locateDefinition",
                    ENSURE_PARSED],
                   "Find in path: reparse"),

        NormalRule(["OCAutoFormatTypedHandler.execute",
                    "PsiUtilBase.getLanguageInEditor",
                    ENSURE_PARSED],
                   "Auto format typed handler: get language and reparse"),

        NormalRule(["FileSymbolTablesCache$OCCodeBlockModificationListener.treeChanged", ENSURE_PARSED],
                   "FileSymbolTablesCache$OCCodeBlockModificationListener.treeChanged"),

        NormalRule(["NextOccurenceAction.go", ENSURE_PARSED],
                   "next occurence -> reparse"),

        NormalRule(["DocumentWindowImpl.isValid",
                    "ShredImpl.isValid",
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

        NormalRule(["CtrlMouseHandler", "getEditorForInjectedLanguageNoCommit", ENSURE_PARSED],
                   "CtrlMouseHandler + injected editor (CPP-11610)"),
    ]
    return rules
