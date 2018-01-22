from rules import NormalRule


def get_rules():
    rules = [
        NormalRule(["CidrFilesViewHelper$2.customizeCellRenderer",
                    "OCSearchScope.getExplicitlySpecifiedProjectSourceFiles"],
                   "drawing project tree https://youtrack.jetbrains.com/issue/CPP-10691"),
        NormalRule(["PotemkinProgress.runInSwingThread"],
                   "Potemkin progress"),
        NormalRule(["AbstractTreeStructureBase.getChildElements",
                    "OCHeaderFileTypeDetector.detect"],
                   "Project view: file type detector"),
        NormalRule(["FileSymbolTablesCache",
                    "FileBasedIndexImpl$ChangedFilesCollector.ensureUpToDateAsync"],
                   "File symbols cache: ensure up-to-date async"),
        NormalRule(["editorActions.EnterHandler"],
                   "Enter handler"),

        NormalRule(["EditorGutterComponentImpl",
                    "OCGotoAction.navigate"],
                   "gutter -> goto"),

        NormalRule(["CidrWatchpointHandler.cleanup"],
                   "WA in stop breakpoint (https://youtrack.jetbrains.com/issue/CPP-11330)"),
    ]
    return rules
