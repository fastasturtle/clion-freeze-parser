from rules import NormalRule, desc


def get_rules():
    rules = [
        NormalRule(["TextEditorPsiDataProvider.getData",
                    "TargetElementUtil.findTargetElement"],
                   desc("getData(PSI_ELEMENT)")),
    ]
    return rules
