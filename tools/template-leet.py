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
from typing import List


# --- ここから ---

        return ret
# --- ここまで提出 ---


ans = Solution().method(
    input(),
    eval(input())
)
print(ans)
