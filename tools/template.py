"""
from math import gcd
from itertools import accumulate, combinations, permutations, product
from bisect import bisect, bisect_left
from collections import Counter, defaultdict, deque
from heapq import heappush, heappop
from functools import reduce
from operator import add, mul, sub, truediv, floordiv, mod

from decimal import *
getcontext().prec = 500

import string
ascii = string.ascii_lowercase
"""
if not __debug__:
    import sys

    f = open(sys.argv[1], "r")
    sys.stdin = f

# --- Submit from here to the end ---
from sys import stdin


def main():
    input = lambda: stdin.readline()[:-1]
    N, M = map(int, input().split())
    A = map(int, input().split())
    A = [int(input()) for _ in [0] * N]
    A = [tuple(map(int, input().split())) for _ in [0] * N]  # [(1, 2), (3, 4)]
    A = [(s, int(t)) for s, t in (input().split() for _ in [0] * N)]  # [('A', 1), ('B', 2), ('C', 3)]
    A = stdin.read().splitlines()  # 複数行を一気に読む
    A, B, C, D = zip(*[map(int, input().split()) for _ in [0] * N])  # 列毎のタプルにする


main()
