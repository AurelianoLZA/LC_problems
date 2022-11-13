import collections
import functools
import math
from typing import List
from typing import Optional

'''

'''


class Solution:
    def myAtoi(self, s: str) -> int:
        ls = list(filter(lambda x : x.isdigit(), list(s)))
        if "-" in s:
            ls.insert(0, "-")
        return int("".join(ls))



sol = Solution()
res = sol.myAtoi(" asc -42 anywords ")
print(res)
