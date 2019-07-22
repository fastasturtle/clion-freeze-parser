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

        NormalRule(["VirtualFileChangeListener.",
                    "com.jetbrains.cidr.lang.symbols.symtable.FileSymbolTablesCache"],
                   desc("FileSymbolTablesCache VFS listener")),

        NormalRule(["build.CidrBuild",
                    "LocalFileSystemBase.refreshAndFindFileByIoFile"],
                   desc("CidrBuild: refresh VFS")),

        NormalRule(["symtable.SerializationServiceImpl",
                    "ApplicationImpl.runReadAction"],
                   desc("Serialization service: read lock (to investigate)")),

        NormalRule(["PsiDocumentManagerImpl.finishCommitInWriteAction",
                    "source.tree.injected",
                    "LazyParseableElement.ensureParsed"],
                   desc("Finish commit: ensure parsed (caused by injection)")),

        NormalRule(["GlobalInspectionContextImpl.inspectFile",
                    "ApplicationImpl.tryRunReadAction"],
                   desc("Global inspections: blocking?")),

        NormalRule(["CidrPathConsoleFilter.processLocalPath"],
                   desc("Slow IO in non-blocking read action")),

        NormalRule(["DefaultHighlightVisitorBasedInspection.runGeneralHighlighting"],
                   desc("Highlighting inspection: blocking?")),

        NormalRule(["TemplateDataLanguagePusher.acceptsFile",
                    "FileTypeManagerImpl.getOrDetectFromContent"],
                   desc("TemplateDataLanguagePusher: file type detector")),

        NormalRule(["SymbolTableProvider.findProvider",
                    "FileTypeManagerImpl.getOrDetectFromContent"],
                   desc("SymbolTableProvider: file type detector")),

        NormalRule(["OCWorkspaceFileListener",
                    "FileTypeManagerImpl.getOrDetectFromContent"],
                   desc("TemplateDataLanguagePusher: file type detector")),

        NormalRule(["OCGlobalUnusedInspection.inspectionFinished"],
                   desc("OCGlobalUnusedInspection not cancelled?")),

        NormalRule(["CMakeWorkspace.projectOpened",
                    "CidrWorkspace.updateContentRoots"],
                   desc("CMake project: update content roots on open")),

    ]
    return rules
