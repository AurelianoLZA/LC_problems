import collections
import functools
import math
from typing import List
from typing import Optional

'''
给定两个字符串 s 和 t ，它们只包含小写字母。

字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。

请找出在 t 中被添加的字母。
'''


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c1, c2 = collections.Counter(s), collections.Counter(t)
        for ch in t:
            if c1.get(ch) != c2.get(ch):
                return ch




if __name__ == '__main__':
    sol = Solution()
    res = sol.findTheDifference("a", "aa")
    print(res)
