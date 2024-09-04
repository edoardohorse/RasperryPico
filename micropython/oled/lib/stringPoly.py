def ljust(s, width, fillchar=' '):
    return s + fillchar * (width - len(s)) if len(s) < width else s

def rjust(s, width, fillchar=' '):
    return fillchar * (width - len(s)) + s if len(s) < width else s