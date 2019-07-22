from rules import NormalRule, desc


def get_rules():
    rules = [
        NormalRule(["OCEvaluator.getExpressionRangeAtOffset"],
                   desc("OCEvaluator.getExpressionRangeAtOffset", bug="CPP-13122")),

        NormalRule(["OCDebuggerTypesHelper.computeSourcePosition"],
                   desc("OCDebuggerTypesHelper.computeSourcePosition", bug="CPP-13122")),

        NormalRule(["CidrDebuggerTypesHelper.findContextElement"],
                   desc("CidrDebuggerTypesHelper.findContextElement", bug="CPP-13122")),

        NormalRule(["OCEvaluatorHelper.convertExpressionPrivate"],
                   desc("OCEvaluatorHelper.convertExpressionPrivate", bug="CPP-13122")),
    ]
    return rules
