from rules import NormalRule, desc


def get_rules():
    rules = [
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

        NormalRule(["LineMarkerInfo.getLineMarkerTooltip",
                    "CidrTestRunConfigurationProducer.setupConfigurationFromContext"],
                   desc("Test line marker: tooltip")),

        NormalRule(["SwiftPackageManagerTestCommandLineState.prepareTestExecutionEnvironment",
                    "ApplicationImpl.runReadAction"],
                   desc("SPM test: blocking read action")),
    ]
    return rules
