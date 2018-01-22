from rules import NormalRule


def get_rules():
    rules = [
        NormalRule(["OCSymbolWithQualifiedName.getLocationString"],
                   "getLocationString() (https://youtrack.jetbrains.com/issue/CPP-10102)"),
        NormalRule(["TextEditorPsiDataProvider.getData", "TargetElementUtil.findTargetElement"],
                   "getData(PSI_ELEMENT)"),
    ]
    return rules
