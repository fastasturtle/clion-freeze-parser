from rules import NormalRule, desc, ENSURE_PARSED


def get_rules():
    rules = [
        NormalRule(["PsiElement2UsageTargetAdapter.isValid",
                    ENSURE_PARSED],
                   desc("usages view", bug="CPP-8459")),

        NormalRule(["UsageInfo2UsageAdapter.isValid",
                    ENSURE_PARSED],
                   desc("usages view", "CPP-8459")),

        NormalRule(["UsageViewImpl.checkNodeValidity",
                    ENSURE_PARSED],
                   desc("usages view", bug="CPP-8459")),

        NormalRule(["BraceHighlightingHandler.lookForInjectedAndMatchBracesInOtherThread",
                    ENSURE_PARSED],
                   desc("brace matcher", bug="IDEA-177314")),

        NormalRule(["FindInPathAction.actionPerformed",
                    "FindInProjectUtil.setDirectoryName",
                    "OCSymbolBase.locateDefinition",
                    ENSURE_PARSED],
                   desc("Find in path: reparse")),

        NormalRule(["OCAutoFormatTypedHandler.execute",
                    "PsiUtilBase.getLanguageInEditor",
                    ENSURE_PARSED],
                   desc("Auto format typed handler: get language and reparse")),

        NormalRule(["FileSymbolTablesCache$OCCodeBlockModificationListener.treeChanged",
                    ENSURE_PARSED],
                   desc("FileSymbolTablesCache$OCCodeBlockModificationListener.treeChanged")),

        NormalRule(["NextOccurenceAction.go",
                    ENSURE_PARSED],
                   desc("next occurence -> reparse")),

        NormalRule(["DocumentWindowImpl.isValid",
                    "ShredImpl.isValid",
                    ENSURE_PARSED],
                   desc("DocumentWindowImpl.isValid -> reparse")),

        NormalRule(["MyAutoScrollFromSourceHandler",
                    "SelectInTargetPsiWrapper.selectIn",
                    ENSURE_PARSED],
                   desc("Autoscroll to source -> reparse", bug="CPP-11591")),

        NormalRule(["GotoDeclarationAction.update",
                    ENSURE_PARSED],
                   desc("Goto declaration update -> reparse")),

        NormalRule(["SelectWordHandler.doExecute",
                    ENSURE_PARSED],
                   desc("Select word/expand selection -> reparse", bug="CPP-11901")),

        NormalRule(["CodeFoldingManagerImpl$1.mouseMoved",
                    ENSURE_PARSED],
                   desc("Folding + mouse moved -> reparse")),

        NormalRule(["TextEditorPsiDataProvider.getData",
                    ENSURE_PARSED],
                   desc("TextEditorPsiDataProvider -> reparse", bug="CPP-11936")),

        NormalRule(["CtrlMouseHandler",
                    "getEditorForInjectedLanguageNoCommit",
                    ENSURE_PARSED],
                   desc("CtrlMouseHandler + injected editor", bug="CPP-11610")),

        NormalRule(["documentation.QuickDocOnMouseOverManager",
                    ENSURE_PARSED],
                   desc("Quick Documentation on mouse move -> reparse", bug="CPP-12831")),

        NormalRule(["editorActions.PasteHandle",
                    ENSURE_PARSED],
                   desc("Paste function from huge header -> reparse", bug="CPP-14849")),

        NormalRule(["editorActions.CutHandler",
                    ENSURE_PARSED],
                   desc("Cut function from huge header -> reparse", bug="CPP-14849")),

        NormalRule(["SmartPointerManagerImpl.updatePointerTargetsAfterReparse",
                    ENSURE_PARSED],
                   desc("Document commit while updating smart psi pointers", bug="CPP-13493")),

    ]
    return rules
