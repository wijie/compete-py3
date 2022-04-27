"""
from fractions import gcd
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

# --- Submit from here ---
class Name:

    return ret
# --- Submit up to here ---

def input_s():
    s = input()
    return [t.strip('"') for t in s[1:-1].split(", ")]


def input_i():
    s = input()
    return [int(t) for t in s[1:-1].split(", ")]


ans = Name().method(input().strip('"'), eval(input()))
print(ans)
