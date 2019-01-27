from rules import NormalRule, desc


def get_rules():
    rules = [
        NormalRule(["CidrFilesViewHelper$2.customizeCellRenderer",
                    "OCSearchScope.getExplicitlySpecifiedProjectSourceFiles"],
                   desc("drawing project tree", bug="CPP-10691", fixed=181)),

        NormalRule(["PotemkinProgress.runInSwingThread"],
                   desc("Potemkin progress", bug="not a bug")),

        NormalRule(["AbstractTreeStructureBase.getChildElements",
                    "OCHeaderFileTypeDetector.detect"],
                   desc("Project view: file type detector")),

        NormalRule(["FileSymbolTablesCache",
                    "FileBasedIndexImpl$ChangedFilesCollector.ensureUpToDateAsync"],
                   desc("File symbols cache: ensure up-to-date async")),

        NormalRule(["editorActions.EnterHandler"],
                   desc("Enter handler")),

        NormalRule(["EditorGutterComponentImpl",
                    "OCGotoAction.navigate"],
                   desc("gutter -> goto")),

        NormalRule(["CidrWatchpointHandler.cleanup"],
                   desc("WA in stop breakpoint", bug="CPP-11330", fixed=181)),

        NormalRule(["Inet4AddressImpl.getLocalHostName"],
                   desc("Slow getLocalHostName", bug="JRE-251", fixed=181)),
    ]
    return rules
