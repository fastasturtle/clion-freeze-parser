from rules import NormalRule, desc


def get_rules():
    rules = [
        # Rename

        NormalRule(["OCRenameProcessor.prepareRenaming"],
                   desc("Rename")),

        NormalRule(["OCInplaceRenameHandler.doRename"],
                   desc("Executing inplace rename", bug="CPP-13833")),

        NormalRule(["refactoring.introduce.inplace.AbstractInplaceIntroducer",
                    "OCBaseExpressionInplaceIntroducer.suggestNames"],
                   desc("Suggesting a name during inplace refactoring", bug="CPP-14932")),
        ###

        NormalRule(["OCCreateNewDefinitionIntentionAction.getText"],
                   desc("Create new Definition", bug="CPP-12939")),

        NormalRule(["OCCCppGenerateHandlerBase.invoke"],
                   desc("CPP generate action")),

        NormalRule(["OCBaseGenerateTestAction.update",
                    "OCBaseGenerateTestAction.isValidForFile"],
                   desc("Generate test: is valid for", bug="CPP-14396")),

        NormalRule(["OCInlineActionHandlerBase.inlineElement"],
                   desc("Inline")),

        NormalRule(["OCExtractMethodHandler.invoke",
                    "OCExtractMethodProcessor.invoke"],
                   desc("Extract method")),

        NormalRule(["EditorGutterComponentImpl.mouseReleased",
                    "OCGotoActionSync.navigate"],
                   desc("Editor gutter: recalculating targets on a click")),

        # Move Action

        NormalRule(["OCSymbolWithQualifiedName.processSameSymbols",
                    "OCAbstractMoveDialog.setMembersChecked"],
                   desc("Move")),

        NormalRule(["OCMoveTopLevelRefactoringHandler.showDialog",
                    "OCDependentMembersCollector.collect"],
                   desc("Move")),

        NormalRule(["OCMoveProcessor"],
                   desc("Move")),

        NormalRule(["OCMoveRefactoringHandler.showDialog"],
                   desc("Move", bug="CPP-14961")),

        NormalRule(["OCMoveHandlerDelegate.tryToMove"],
                   desc("Move after editing common header", bug="CPP-14352")),

        ###
        NormalRule(["OCChangeSignatureProcessor.runSynchronously",
                    "OCChangeSignatureUsageProcessor.findConflicts"],
                   desc("Change signature: find conflicts")),

        # Change signature

        NormalRule(["OCChangeSignatureProcessor.preprocessUsages"],
                   desc("Change signature: preprocessUsages")),

        NormalRule(["ChangeSignatureAction.isAvailableOnElementInEditorAndFile",
                    "OCChangeSignatureActionHandler.findTargetMember"],
                   desc("Change signature: isAvailable from EDT")),



        NormalRule(["LoadCMakeProjectAction.actionPerformed"],
                   desc("Load CMake project", bug="CPP-14237")),

        ###

        # Find Usage
        NormalRule(["OCSymbolWithQualifiedNameImpl.processAssociatedSymbols",
                    "FindUsagesAction.actionPerformed"],
                   desc("Find usages search associated targets", bug="CPP-12806")),

        NormalRule(["OCSymbolWithQualifiedNameImpl.getDefinitionSymbol",
                    "FindUsagesAction.actionPerformed"],
                   desc("Find usages search definitions", bug="CPP-14785")),

        NormalRule(["ShowUsagesAction.actionPerformed",
                    "ShowUsagesAction.showElementUsages",
                    "UsageInfo.<init>"],
                   desc("Show usages action: sync resolve")),

        ###

        NormalRule(["SearchAgainAction.actionPerformed"],
                   desc("Search again", bug="CPP-14288")),

        NormalRule(["ImportCMakeProjectAction.actionPerformed"],
                   desc("Import CMake Project", bug="CPP-14495")),

        NormalRule(["mac.touchbar.TouchBar"],
                   desc("Touchbar action updates might lead to freezes", bug="CPP-14495")),

        NormalRule(["com.intellij.codeInsight.completion.CodeCompletionHandlerBase"],
                   desc("Code completion", bug="CPP-14780")),

        NormalRule(["com.intellij.ide.ui.laf.darcula.ui.TextFieldWithPopupHandlerUI"],
                   desc("Deadlock on Search Everywhere", bug="IDEA-196919")),

        NormalRule(["actions.DeleteAction.actionPerformed",
                    "projectView.impl.ProjectViewImpl"],
                   desc("Delete build directory may lead the freeze", bug="CPP-14872")),

        NormalRule(["actions.PasteReferenceProvider.isPasteEnabled",
                    "QualifiedNameProviderUtil.qualifiedNameToElement"],
                   desc("Paste handler resolves in EDT", bug="CPP-12414")),

        NormalRule(["OCSwitchToHeaderOrSourceRelatedProvider.",
                    "ApplicationImpl.runReadAction"],
                   desc("Switch to header/source: blocking read action")),

        NormalRule(["FindUsagesHandler.processElementUsages",
                    "ApplicationImpl.runReadAction"],
                   desc("Find usages: blocking read action")),

        NormalRule(["OCCreateNewDefinitionIntentionAction.isAvailable"],
                   desc("OCCreateNewDefinitionIntentionAction: isAvailable")),

        NormalRule(["FoldingModelSupport.getLineSeparatorDescription",
                    "ApplicationImpl.runReadAction"],
                   desc("Diff breadcrumbs: blocking read action", bug="IDEA-216929")),

        NormalRule(["OCGotoActionAsync.navigate",
                    "AbstractQuery.findFirst"],
                   desc("Async goto: findFirst")),


        NormalRule(["SafeDeleteHandler.invoke",
                    "OCFindUsagesHandlerFactory.createFindUsagesHandler",
                    "OCSymbolWithQualifiedNameImpl.processAssociatedSymbols"],
                   desc("SafeDeleteHandler: assoc symbol")),

        NormalRule(["GotoImplementationHandler.getSourceAndTargetElements"],
                   desc("Goto implementation")),

        NormalRule(["OCRemoveDeclarationButInitializerIntentionAction.isAvailable"],
                   desc("OCRemoveDeclarationButInitializerIntentionAction.isAvailable")),

        NormalRule(["OCFindUsagesHandler.getPrimaryElements",
                    "ShowUsagesAction.showElementUsages"],
                   desc("Show usages: find primary element")),

        NormalRule(["OCAsyncParamInfoModelImpl$calculateFirstResult",
                    "ApplicationImpl.runReadAction"],
                   desc("param info: blocking calculate first result")),

        NormalRule(["OCInvertIfConditionIntentionAction.invoke"],
                   desc("OCInvertIfConditionIntentionAction invoke")),

        NormalRule(["OCResolveConfigurationImpl.updateFilesCache"],
                   desc("OCResolveConfigurationImpl.updateFilesCache")),

        NormalRule(["OCHeaderGuardRenameProcessor.skipNonCodeUsage",
                    "OCHeaderGuardDetector.visitElement"],
                   desc("header guard renamer: skip non code usages")),

        NormalRule(["OCParameterInplaceIntroducer.introduceForReal",
                    "OCChangeSignatureProcessor.runSynchronously"],
                   desc("Change signature during introduce refactoring")),

        NormalRule(["OCInplaceRenamer.checkLocalScope"],
                   desc("OCInplaceRenamer.checkLocalScope")),

        NormalRule(["FindUsagesAction.actionPerformed",
                    "TargetElementUtil.findTargetElement"],
                   desc("Find Usages action finds target element on EDT")),

        NormalRule(["GotoDeclarationAction.suggestCandidates",
                    "TargetElementUtil.getTargetCandidates",
                    "resolve"],
                   desc("Go to declaration suggest candidates", bug="CPP-17071")),

    ]
    return rules
