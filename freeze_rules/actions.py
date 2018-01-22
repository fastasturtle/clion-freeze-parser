from rules import NormalRule


def get_rules():
    rules = [
        NormalRule(["OCRenameProcessor.prepareRenaming"],
                   "Rename"),

        NormalRule(["OCInplaceRenameHandler.doRename"],
                   "Rename"),

        NormalRule(["OCCreateNewDefinitionIntentionAction.getText"],
                   "OCCreateNewDefinitionIntentionAction.getText"),

        NormalRule(["OCCCppGenerateHandlerBase.invoke"],
                   "CPP generate action"),

        NormalRule(["OCGotoDeclarationHandler.getActionText"],
                   "goto declaration action text https://youtrack.jetbrains.com/issue/CPP-8460"),

        NormalRule(["OCArgumentListCallPlace.collectCallOptions"],
                   "parameter info https://youtrack.jetbrains.com/issue/CPP-9361"),

        NormalRule(["OCFunctionParameterInfoHandler.updateParameterInfo"],
                   "parameter info https://youtrack.jetbrains.com/issue/CPP-9361"),

        NormalRule(["OCSwitchToHeaderOrSourceRelatedProvider.getItems"],
                   "switch to source/header https://youtrack.jetbrains.com/issue/CPP-7168"),

        NormalRule(["OCImportSymbolFix.showHint",
                    "OCStructSymbol.getKindUppercase"],
                   "Import symbol fix https://youtrack.jetbrains.com/issue/CPP-10663"),
        NormalRule(["OCBaseGenerateTestAction.update",
                    "OCBaseGenerateTestAction.isValidForFile"],
                   "Generate test: is valid for"),

        NormalRule(["OCInlineActionHandlerBase.inlineElement"], "Inline"),

        NormalRule(["OCExtractMethodHandler.invoke",
                    "OCExtractMethodProcessor.invoke"],
                   "Extract method"),

        NormalRule(["OCSymbolWithQualifiedName.processSameSymbols",
                    "OCAbstractMoveDialog.setMembersChecked"],
                   "Move"),

        NormalRule(["com.jetbrains.cidr.lang.refactoring.move.handlers.OCMoveTopLevelRefactoringHandler.showDialog",
                    "com.jetbrains.cidr.lang.refactoring.move.OCDependentMembersCollector.collect"],
                   "Move"),

        NormalRule(["com.jetbrains.cidr.lang.refactoring.move.OCMoveProcessor"],
                   "Move"),

        NormalRule(["OCMoveRefactoringHandler.showDialog"],
                   "Move"),

        NormalRule(["OCCppDefinitionsUtil.getOutsidePreferredPosition", "OCSplitFunctionIntentionAction.invoke"],
                   "Split function (https://youtrack.jetbrains.com/issue/CPP-11254)"),

        NormalRule(["OCGenerateUtil.applyReplacements", "OCImportSymbolFix.fixAllSymbolsRecursively"],
                   "Generate definition: import fix"),

        NormalRule(["OCChangeSignatureProcessor.runSynchronously",
                    "OCChangeSignatureUsageProcessor.findConflicts"],
                   "Change signature: find conflicts"),

        NormalRule(["OCChangeSignatureProcessor.preprocessUsages"],
                   "Change signature: preprocessUsages"),
    ]
    return rules
