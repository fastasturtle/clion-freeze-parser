from freeze_rules.util import desc
from rules import NormalRule


def get_rules():
    rules = [
        NormalRule(["OCTypedHandlerDelegate.charTyped", "PsiDocumentManagerBase.commitDocument"],
                   desc("commit on typing", "CPP-11365")),

    ]
    return rules
