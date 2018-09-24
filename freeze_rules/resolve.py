from rules import NormalRule, desc


def get_rules():
    rules = [
        NormalRule(["OCSymbolWithQualifiedName.getLocationString"],
                   desc("getLocationString()", "CPP-10102", fixed="review")),

        NormalRule(["TextEditorPsiDataProvider.getData",
                    "TargetElementUtil.findTargetElement"],
                   desc("getData(PSI_ELEMENT)")),
    ]
    return rules
