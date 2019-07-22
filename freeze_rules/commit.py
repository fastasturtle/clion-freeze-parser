from rules import NormalRule, desc


def get_rules():
    rules = [
        NormalRule(["OCTypedHandlerDelegate.charTyped",
                    "PsiDocumentManagerBase.commitDocument"],
                   desc("commit on typing", bug="CPP-11365", fixed=181)),

        NormalRule(["CopyHandler.doExecute",
                    "PsiDocumentManagerBase.doCommit"],
                   desc("CopyHandler: commit")),

        NormalRule(["CodeInsightAction.beforeActionPerformedUpdate",
                    "PsiDocumentManagerBase.doCommit"],
                   desc("CodeInsightAction: before action commit")),

        NormalRule(["SelectWordHandler.doExecute",
                    "PsiDocumentManagerBase.doCommit"],
                   desc("SelectWordHandler commit")),

        NormalRule(["ReformatCodeAction.actionPerformed",
                    "PsiDocumentManagerBase.doCommit"],
                   desc("Reformat action commit")),

        NormalRule(["AutoIndentLinesAction",
                    "PsiDocumentManagerBase.doCommit"],
                   desc("AutoIndentLinesAction commit")),

        NormalRule(["CodeInsightEditorAction.beforeActionPerformedUpdate",
                    "PsiDocumentManagerBase.doCommit"],
                   desc("CodeInsightEditorAction commit")),
    ]
    return rules
