import sys, os
from pathlib import Path

def add_src_folders():
    src_folders = [x[0] for x in os.walk(Path(__file__, '..', '..').resolve())]

    for folders in src_folders:
        sys.path.append(folders)