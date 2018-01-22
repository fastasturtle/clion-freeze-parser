from freeze_rules.util import desc
from rules import NormalRule


def get_rules():
    rules = [
        NormalRule(["OCSymbolWithQualifiedName.getLocationString"],
                   desc("getLocationString()", "CPP-10102", fixed="review")),
        NormalRule(["TextEditorPsiDataProvider.getData", "TargetElementUtil.findTargetElement"],
                   desc("getData(PSI_ELEMENT)")),
    ]
    return rules
