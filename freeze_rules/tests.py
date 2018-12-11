from rules import NormalRule, desc


def get_rules():
    rules = [
        NormalRule(["CidrTestWithScopeElementsFramework.getTestLinks"],
                   desc("CidrTestWithScopeElementsFramework.getTestLinks", bug="CPP-11735", fixed=183)),

        NormalRule(["Utils.fillMenu",
                    "CidrTestRunConfigurationProducer.isConfigurationFromContext"],
                   desc("Context configuration click", bug="CPP-9359")),

        NormalRule(["CidrRunConfigurationSettingsEditor$MyComboBox.fireSelectedItemChanged",
                    "CidrGoogleTestRunConfigurationData"],
                   desc("Google test run configuration editor")),

        NormalRule(["cidr.execution.testing.CidrTestListUpdater"],
                   desc("Initial tests scanning in big projects", bug="CPP-14242")),

        NormalRule(["cidr.execution.testing.google.CidrGoogleTestRunConfigurationData.checkData"],
                   desc("Initial tests scanning in big projects", bug="CPP-14242")),
    ]
    return rules
