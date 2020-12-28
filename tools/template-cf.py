'''
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
'''
from sys import stdin


def main():
    input = lambda: stdin.readline()[:-1]
    T = int(input())
    for _ in [0] * T:
        N = int(input())
        N, M = map(int, input().split())
        A = map(int, input().split())
        L = [int(input()) for _ in [0] * N]
        L = [tuple(map(int, input().split())) for _ in [0] * N]  # [(1, 2), (3, 4)]
        L = [(i, int(j)) for i, j in (input().split() for _ in [0] * N)]  # [('A', 1), ('B', 2), ('C', 3)]
        L = stdin.read().splitlines()  # 複数行を一気に読む
        D = dict(map(int, input().split()) for _ in [0] * N)  # {1: 2, 3: 4}
        D = {i: int(input()) for i in range(N)}
        D = {i: int(j) for i, j in enumerate(input().split(), start=1)}
        A, B, C, D = (int(input()) for _ in [0] * 4)


main()
