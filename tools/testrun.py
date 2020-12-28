#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Task Run for Competitive programming
'''
import os
import argparse
import subprocess
from timeit import timeit


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='python script')
    parser.add_argument('--time', help='show Exec Time', action='store_true')
    args = parser.parse_args()

    ext = os.path.splitext(args.file)[1]
    cmd = {
        '.py' : ['python3', args.file],
        '.rb' : ['ruby', args.file]
    }.get(ext, args.file)

    infile = 'input.txt'
    testcase = '.testcase'
    with open(infile, 'r') as fi:
        test = [s.strip() for s in fi.read().split('\n\n') if s.strip()]
    for i, val in enumerate(test):
        if i:
            print()
        with open(testcase, 'w') as fo:
            fo.write(val + '\n')
        with open(testcase, 'r') as fi:
            if args.time:
                result = timeit(lambda: subprocess.run(cmd, stdin=fi), number=1)
                elapsed_time = round(result * 1000)
                print('Exec Time:', '{:,}'.format(elapsed_time), 'ms')
            else:
                subprocess.run(cmd, stdin=fi)


if __name__ == '__main__':
    main()
