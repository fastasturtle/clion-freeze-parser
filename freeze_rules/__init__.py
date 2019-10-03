import pkgutil
import os

import freeze_rules.actions
import freeze_rules.commit
import freeze_rules.lazyReparse
import freeze_rules.misc
import freeze_rules.plugin
import freeze_rules.resolve
import freeze_rules.tests
import freeze_rules.clangd
import freeze_rules.debugger

import freeze_rules.fixed


def get_rules():
    rules = []
    for (i, name, _) in pkgutil.iter_modules([os.path.dirname(__file__)]):
        rules += eval(name + '.get_rules()')
    return rules
