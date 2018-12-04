from rules import NormalRule, desc


def get_rules():
    rules = [
        NormalRule(["OCRenameProcessor.prepareRenaming"],
                   desc("Rename")),

        NormalRule(["OCInplaceRenameHandler.doRename"],
                   desc("Rename", bug="CPP-14434")),

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

        NormalRule(["OCMoveHandlerDelegate.tryToMove"],
                   desc("Move after editing common header", bug="CPP-14352")),

        NormalRule(["OCCppDefinitionsUtil.getOutsidePreferredPosition",
                    "OCSplitFunctionIntentionAction.invoke"],
                   desc("Split function", bug="CPP-11254")),

        NormalRule(["OCGenerateUtil.applyReplacements",
                    "OCImportSymbolFix.fixAllSymbolsRecursively"],
                   desc("Generate definition: import fix", fixed="review")),

        NormalRule(["OCChangeSignatureProcessor.runSynchronously",
                    "OCChangeSignatureUsageProcessor.findConflicts"],
                   desc("Change signature: find conflicts")),

        NormalRule(["OCChangeSignatureProcessor.preprocessUsages"],
                   desc("Change signature: preprocessUsages")),

        NormalRule(["LoadCMakeProjectAction.actionPerformed"],
                   desc("Load CMake project", "CPP-14237")),

        NormalRule(["OCSymbolWithQualifiedNameImpl.processAssociatedSymbols",
                    "FindUsagesAction.actionPerformed"],
                   desc("Find usages search associated targets", "CPP-12806")),

        NormalRule(["OCSymbolWithQualifiedNameImpl.getDefinitionSymbol",
                    "FindUsagesAction.actionPerformed"],
                   desc("Find usages search definitions", "CPP-14785")),

        NormalRule(["SearchAgainAction.actionPerformed"],
                   desc("Search again", "CPP-14288")),

        NormalRule(["ImportCMakeProjectAction.actionPerformed"],
                   desc("Import CMake Project", "CPP-14495")),

        NormalRule(["mac.touchbar.TouchBar"],
                   desc("Touchbar action updates might lead to freezes", "CPP-14495")),

        NormalRule(["com.intellij.codeInsight.completion.CodeCompletionHandlerBase"],
                   desc("Code completion", "CPP-14780")),

        NormalRule(["com.intellij.ide.ui.laf.darcula.ui.TextFieldWithPopupHandlerUI"],
                   desc("Deadlock on Search Everywhere", "IDEA-196919")),

        NormalRule(["actions.DeleteAction.actionPerformed",
                    "projectView.impl.ProjectViewImpl"],
                   desc("Delete build directory may lead the freeze", "CPP-14872")),
    ]
    return rules
