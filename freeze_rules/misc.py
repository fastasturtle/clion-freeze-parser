from rules import NormalRule, desc


def get_rules():
    rules = [
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
    ]
    return rules
