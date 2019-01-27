from rules import NormalRule, desc


def get_rules():
    rules = [
        NormalRule(["xpathView.XPathAppComponent"],
                   desc("xPathView plugin", bug="IDEA-199079"))
    ]

    return rules

