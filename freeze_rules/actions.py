from freeze_rules.util import desc
from rules import NormalRule


def get_rules():
    rules = [
        NormalRule(["OCRenameProcessor.prepareRenaming"],
                   desc("Rename")),

        NormalRule(["OCInplaceRenameHandler.doRename"],
                   desc("Rename")),

        NormalRule(["OCCreateNewDefinitionIntentionAction.getText"],
                   desc("OCCreateNewDefinitionIntentionAction.getText")),

        NormalRule(["OCCCppGenerateHandlerBase.invoke"],
                   desc("CPP generate action")),

        NormalRule(["OCGotoDeclarationHandler.getActionText"],
                   desc("goto declaration action text", "CPP-8460", fixed=173)),

        NormalRule(["OCArgumentListCallPlace.collectCallOptions"],
                   desc("parameter info", "CPP-9361")),

        NormalRule(["OCFunctionParameterInfoHandler.updateParameterInfo"],
                   desc("parameter info", "CPP-9361")),

        NormalRule(["OCSwitchToHeaderOrSourceRelatedProvider.getItems"],
                   desc("switch to source/header", "CPP-7168")),

        NormalRule(["OCImportSymbolFix.showHint",
                    "OCStructSymbol.getKindUppercase"],
                   desc("Import symbol fix", "CPP-10663", fixed=181)),

        NormalRule(["OCBaseGenerateTestAction.update",
                    "OCBaseGenerateTestAction.isValidForFile"],
                   desc("Generate test: is valid for")),

        NormalRule(["OCInlineActionHandlerBase.inlineElement"],
                   desc("Inline")),

        NormalRule(["OCExtractMethodHandler.invoke",
                    "OCExtractMethodProcessor.invoke"],
                   desc("Extract method")),

        NormalRule(["OCSymbolWithQualifiedName.processSameSymbols",
                    "OCAbstractMoveDialog.setMembersChecked"],
                   desc("Move")),

        NormalRule(["OCMoveTopLevelRefactoringHandler.showDialog",
                    "OCDependentMembersCollector.collect"],
                   desc("Move")),

        NormalRule(["OCMoveProcessor"],
                   desc("Move")),

        NormalRule(["OCMoveRefactoringHandler.showDialog"],
                   desc("Move")),

        NormalRule(["OCCppDefinitionsUtil.getOutsidePreferredPosition",
                    "OCSplitFunctionIntentionAction.invoke"],
                   desc("Split function", "CPP-11254")),

        NormalRule(["OCGenerateUtil.applyReplacements",
                    "OCImportSymbolFix.fixAllSymbolsRecursively"],
                   desc("Generate definition: import fix", fixed="review")),

        NormalRule(["OCChangeSignatureProcessor.runSynchronously",
                    "OCChangeSignatureUsageProcessor.findConflicts"],
                   desc("Change signature: find conflicts")),

        NormalRule(["OCChangeSignatureProcessor.preprocessUsages"],
                   desc("Change signature: preprocessUsages")),
    ]
    return rules
