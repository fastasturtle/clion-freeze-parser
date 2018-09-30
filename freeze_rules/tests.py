from rules import NormalRule, desc


def get_rules():
    rules = [
        NormalRule(["CidrTestWithScopeElementsFramework.getTestLinks"],
                   desc("CidrTestWithScopeElementsFramework.getTestLinks")),

        NormalRule(["Utils.fillMenu",
                    "CidrTestRunConfigurationProducer.isConfigurationFromContext"],
                   desc("Context configuration click")),

        NormalRule(["CidrRunConfigurationSettingsEditor$MyComboBox.fireSelectedItemChanged",
                    "CidrGoogleTestRunConfigurationData"],
                   desc("Google test run configuration editor")),
    ]
    return rules
