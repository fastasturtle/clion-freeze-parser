from rules import NormalRule, desc


def get_rules():
    rules = [
        NormalRule(["ClangDaemonFormatProvider.findClangFormatContent",
                    "CompletableFuture.get"],
                   desc("ClangFormat: findClangFormatContent")),
        NormalRule(["ClangDaemonFormatProvider.format",
                    "DocumentImpl.doGetText"],
                   desc("ClangFormat: slow Document.getText")),
        NormalRule(["PopupActionsKt.hasDisabledOptionHintInfo",
                    "com.jetbrains.cidr.lang.daemon.clang.namehint.ClangInlayParameterHintsProvider.getNamehints",
                    "ClangUtils.waitForClangFuture"],
                   desc("clangd: slow 'has namehints' check")),
    ]
    return rules
