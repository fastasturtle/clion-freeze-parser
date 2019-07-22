from rules import NormalRule, desc


def get_rules():
    rules = [
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
