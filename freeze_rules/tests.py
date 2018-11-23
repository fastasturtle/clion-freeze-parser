from rules import NormalRule, desc


def get_rules():
    rules = [
        NormalRule(["CidrTestWithScopeElementsFramework.getTestLinks"],
                   desc("CidrTestWithScopeElementsFramework.getTestLinks", "CPP-11735", fixed=183)),

        NormalRule(["Utils.fillMenu",
                    "CidrTestRunConfigurationProducer.isConfigurationFromContext"],
                   desc("Context configuration click")),

        NormalRule(["CidrRunConfigurationSettingsEditor$MyComboBox.fireSelectedItemChanged",
                    "CidrGoogleTestRunConfigurationData"],
                   desc("Google test run configuration editor")),
    ]
    return rules
