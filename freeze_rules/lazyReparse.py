from freeze_rules.util import desc
from rules import NormalRule
ENSURE_PARSED = "LazyParseableElement.getFirstChildNode"


def get_rules():
    rules = [
        NormalRule(["PsiElement2UsageTargetAdapter.isValid", ENSURE_PARSED],
                   desc("usages view", "CPP-8459")),
        NormalRule(["UsageInfo2UsageAdapter.isValid", ENSURE_PARSED],
                   desc("usages view", "CPP-8459")),
        NormalRule(["UsageViewImpl.checkNodeValidity", ENSURE_PARSED],
                   desc("usages view", "CPP-8459")),

        NormalRule(["BraceHighlightingHandler.lookForInjectedAndMatchBracesInOtherThread", ENSURE_PARSED],
                   desc("brace matcher", "IDEA-177314")),

        NormalRule(["ComponentStoreImpl.save",
                    "TextEditorState.getFoldingState", ENSURE_PARSED],
                   desc("Save folding state", "CPP-10639", fixed=173)),
        NormalRule(["CodeFoldingManagerImpl.writeFoldingState", ENSURE_PARSED],
                   desc("Save folding state", "CPP-10639", fixed=173)),
        NormalRule(["CodeFoldingManagerImpl.saveFoldingState", ENSURE_PARSED],
                   desc("Save folding state", "CPP-10639", fixed=173)),

        NormalRule(["HighlightUsagesHandlerFactoryBase.createHighlightUsagesHandler", ENSURE_PARSED],
                   desc("create IdentifierHighlighterPass pass", "CPP-9373", fixed=181)),

        NormalRule(["SearchEverywhereAction", "OCSymbolBase.canNavigate", ENSURE_PARSED],
                   desc("Search everywhere -> canNavigate -> reparse")),

        NormalRule(["FileHyperlinkInfoBase.navigate", ENSURE_PARSED],
                   desc("File hyper links: reparse", "CPP-11601", fixed=181)),

        NormalRule(["FindInPathAction.actionPerformed",
                    "FindInProjectUtil.setDirectoryName",
                    "OCSymbolBase.locateDefinition",
                    ENSURE_PARSED],
                   desc("Find in path: reparse")),

        NormalRule(["OCAutoFormatTypedHandler.execute",
                    "PsiUtilBase.getLanguageInEditor",
                    ENSURE_PARSED],
                   desc("Auto format typed handler: get language and reparse")),

        NormalRule(["FileSymbolTablesCache$OCCodeBlockModificationListener.treeChanged", ENSURE_PARSED],
                   desc("FileSymbolTablesCache$OCCodeBlockModificationListener.treeChanged")),

        NormalRule(["NextOccurenceAction.go", ENSURE_PARSED],
                   desc("next occurence -> reparse")),

        NormalRule(["DocumentWindowImpl.isValid",
                    "ShredImpl.isValid",
                    ENSURE_PARSED],
                   desc("DocumentWindowImpl.isValid -> reparse")),

        NormalRule(["MyAutoScrollFromSourceHandler", "SelectInTargetPsiWrapper.selectIn", ENSURE_PARSED],
                   desc("Autoscroll to source -> reparse")),

        NormalRule(["GotoDeclarationAction.update", ENSURE_PARSED],
                   desc("Goto declaration update -> reparse")),

        NormalRule(["SelectWordHandler.doExecute", ENSURE_PARSED],
                   desc("Select word/expand selection -> reparse", "CPP-11901")),

        NormalRule(["CodeFoldingManagerImpl$1.mouseMoved", ENSURE_PARSED],
                   desc("Folding + mouse moved -> reparse")),

        NormalRule(["TextEditorPsiDataProvider.getData", ENSURE_PARSED],
                   desc("TextEditorPsiDataProvider -> reparse", "CPP-11936")),

        NormalRule(["CtrlMouseHandler", "getEditorForInjectedLanguageNoCommit", ENSURE_PARSED],
                   desc("CtrlMouseHandler + injected editor", "CPP-11610")),
    ]
    return rules
