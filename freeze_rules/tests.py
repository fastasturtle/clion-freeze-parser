from rules import NormalRule


def get_rules():
    rules = [
        NormalRule(["CidrTestWithScopeElementsFramework.getTestLinks"],
                   "CidrTestWithScopeElementsFramework.getTestLinks"),
        NormalRule(["Utils.fillMenu",
                    "CidrTestRunConfigurationProducer.isConfigurationFromContext"],
                   "Context configuration click"),
        NormalRule(["CidrRunConfigurationSettingsEditor$MyComboBox.fireSelectedItemChanged",
                    "CidrGoogleTestRunConfigurationData"],
                   "Google test run configuration editor"),
    ]
    return rules
