from rules import NormalRule, desc


def get_rules():
    rules = [
        NormalRule(["OCSymbolWithQualifiedName.getLocationString"],
                   desc("getLocationString()", bug="CPP-10102", fixed=181)),

        NormalRule(["TextEditorPsiDataProvider.getData",
                    "TargetElementUtil.findTargetElement"],
                   desc("getData(PSI_ELEMENT)")),
    ]
    return rules
