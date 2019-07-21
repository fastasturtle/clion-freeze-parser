from rules import NormalRule, desc, ENSURE_PARSED


def get_rules():
    rules = [
        NormalRule(["OCGotoDeclarationHandler.getActionText"],
                   desc("Go to declaration action text", bug="CPP-8460", fixed=173)),

        NormalRule(["OCArgumentListCallPlace.collectCallOptions"],
                   desc("parameter info", bug="CPP-9361", fixed=182)),

        NormalRule(["OCFunctionParameterInfoHandler.updateParameterInfo"],
                   desc("parameter info", bug="CPP-9361", fixed=182)),

        NormalRule(["OCSwitchToHeaderOrSourceRelatedProvider.getItems"],
                   desc("switch to source/header", bug="CPP-7168", fixed=182)),

        NormalRule(["OCImportSymbolFix.showHint",
                    "OCStructSymbol.getKindUppercase"],
                   desc("Import symbol fix", bug="CPP-10663", fixed=181)),

        NormalRule(["OCCppDefinitionsUtil.getOutsidePreferredPosition",
                    "OCSplitFunctionIntentionAction.invoke"],
                   desc("Split function", bug="CPP-11254", fixed=182)),

        NormalRule(["OCGenerateUtil.applyReplacements",
                    "OCImportSymbolFix.fixAllSymbolsRecursively"],
                   desc("Generate definition: import fix", fixed="review")),

        NormalRule(["OCTypedHandlerDelegate.charTyped",
                    "PsiDocumentManagerBase.commitDocument"],
                   desc("commit on typing", bug="CPP-11365", fixed=181)),

        NormalRule(["CidrFilesViewHelper$2.customizeCellRenderer",
                    "OCSearchScope.getExplicitlySpecifiedProjectSourceFiles"],
                   desc("drawing project tree", bug="CPP-10691", fixed=181)),

        NormalRule(["CidrWatchpointHandler.cleanup"],
                   desc("WA in stop breakpoint", bug="CPP-11330", fixed=181)),

        NormalRule(["Inet4AddressImpl.getLocalHostName"],
                   desc("Slow getLocalHostName", bug="JRE-251", fixed=181)),

        NormalRule(["OCSymbolWithQualifiedName.getLocationString"],
                   desc("getLocationString()", bug="CPP-10102", fixed=181)),

        NormalRule(["CidrTestWithScopeElementsFramework.getTestLinks"],
                   desc("CidrTestWithScopeElementsFramework.getTestLinks", bug="CPP-11735", fixed=183)),

        NormalRule(["ComponentStoreImpl.save",
                    "TextEditorState.getFoldingState",
                    ENSURE_PARSED],
                   desc("Save folding state", "CPP-10639", fixed=173)),

        NormalRule(["CodeFoldingManagerImpl.writeFoldingState",
                    ENSURE_PARSED],
                   desc("Save folding state", "CPP-10639", fixed=173)),

        NormalRule(["CodeFoldingManagerImpl.saveFoldingState",
                    ENSURE_PARSED],
                   desc("Save folding state", "CPP-10639", fixed=173)),

        NormalRule(["HighlightUsagesHandlerFactoryBase.createHighlightUsagesHandler",
                    ENSURE_PARSED],
                   desc("create IdentifierHighlighterPass pass", bug="CPP-9373", fixed=181)),

        NormalRule(["SearchEverywhereAction", "OCSymbolBase.canNavigate",
                    ENSURE_PARSED],
                   desc("Search everywhere -> canNavigate -> reparse", bug="CPP-11711", fixed=182)),

        NormalRule(["FileHyperlinkInfoBase.navigate",
                    ENSURE_PARSED],
                   desc("File hyper links: reparse", bug="CPP-11601", fixed=181)),

    ]
    return rules
