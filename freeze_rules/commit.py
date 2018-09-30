from rules import NormalRule, desc


def get_rules():
    rules = [
        NormalRule(["OCTypedHandlerDelegate.charTyped",
                    "PsiDocumentManagerBase.commitDocument"],
                   desc("commit on typing", "CPP-11365")),

    ]
    return rules
