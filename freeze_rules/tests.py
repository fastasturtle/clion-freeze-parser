from rules import NormalRule


def get_rules():
    rules = [
        NormalRule(["CidrTestWithScopeElementsFramework.getTestLinks"],
                   "CidrTestWithScopeElementsFramework.getTestLinks"),
        NormalRule(["com.intellij.openapi.actionSystem.impl.Utils.fillMenu",
                    "com.jetbrains.cidr.execution.testing.CidrTestRunConfigurationProducer.isConfigurationFromContext"],
                   "Context configuration click"),
        NormalRule(["CidrRunConfigurationSettingsEditor$MyComboBox.fireSelectedItemChanged",
                    "CidrGoogleTestRunConfigurationData"],
                   "Google test run configuration editor"),

    ]
    return rules
