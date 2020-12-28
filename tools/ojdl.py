#! /usr/bin/env python3 -B
# -*- coding: utf-8 -*-

'''
test case downloader
require online-judge-tools

usage: ojdl.py url
'''
import sys
import os
import subprocess
import argparse
from glob import glob


def main() -> None:
    files = glob('./test/*')
    _ = [os.remove(f) for f in files]

    args = sys.argv
    platform = sys.platform  # 'darwin', 'linux', 'win32', 'cygwin'
    if platform == 'darwin':
        if len(args) > 1:
            url = args[1]
        else:
            home = os.path.expanduser('~')
            geturl = ['osascript',
                      '-l',
                      'JavaScript',
                      home + '/bin/geturl-j.applescript']
            url = subprocess.run(geturl, stdout=subprocess.PIPE)
            url = url.stdout.decode('UTF-8').rstrip()
    else:
        parser = argparse.ArgumentParser()
        parser.add_argument('url', help='https://...')
        args = parser.parse_args()
        url = args.url

    subprocess.run(['oj', 'dl', url])


if __name__ == '__main__':
    main()
