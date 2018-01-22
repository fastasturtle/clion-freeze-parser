from rules import NormalRule


def get_rules():
    rules = [
        NormalRule(["OCTypedHandlerDelegate.charTyped", "PsiDocumentManagerBase.commitDocument"],
                   "commit on typing https://youtrack.jetbrains.com/issue/CPP-11365"),

    ]
    return rules
