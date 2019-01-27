from rules import NormalRule, desc


def get_rules():
    rules = [
        NormalRule(["OCTypedHandlerDelegate.charTyped",
                    "PsiDocumentManagerBase.commitDocument"],
                   desc("commit on typing", bug="CPP-11365", fixed=181)),
    ]
    return rules
