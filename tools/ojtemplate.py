#!/usr/bin/env python3

import os
import shutil
import sys
from glob import glob


def main() -> None:
    args = sys.argv
    ext = os.path.splitext(args[1])
    srcdir = os.path.dirname(os.path.realpath(__file__))

    temp = {
        '.py': 'template.py',
        '.cpp': 'template.cpp',
        '': 'template.py'
    }.get(ext[1])

    src = os.path.join(srcdir, temp)
    dest = args[1] if ext[1] else args[1] + os.path.splitext(temp)[1]

    if glob('./template*'):
        src = glob('./template*')[0]
    shutil.copyfile(src, dest)


if __name__ == '__main__':
    main()
