import os

def expand(path):
    if path:
        return os.path.normpath(os.path.expanduser(path))
