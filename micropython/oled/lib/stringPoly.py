import sys

def ljust(s, width, fillchar=' '):
    return s + fillchar * (width - len(s)) if len(s) < width else s

def rjust(s, width, fillchar=' '):
    return fillchar * (width - len(s)) + s if len(s) < width else s

def cleanLastNChar(word:str):
  sys.stdout.write("\b" * len(word))
  sys.stdout.write(" " * len(word))
  sys.stdout.write("\b" * len(word))

def cleanLastLine():
  sys.stdout.write("\033[F")  # Move cursor up one line
  sys.stdout.write("\033[K")  # Move cursor to the end of the current line