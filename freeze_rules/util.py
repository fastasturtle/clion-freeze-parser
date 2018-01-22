def desc(text, bug="CPP-?????", fixed=None):
    fixed_text = ("fixed in " + str(fixed) + " " if fixed else "")
    return fixed_text + text + " (" + bug + ")"
