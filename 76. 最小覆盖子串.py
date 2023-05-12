import collections
import functools
import math
from typing import List
from typing import Optional

'''
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。
如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

// 2个超时，问题不大，不管了
265 / 267

'''


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def helper(c1:dict, c2:dict):
            for key, val in c2.items():
                if key not in c1.keys() or val > c1.get(key):
                    return False
            return True

        left, right = 0, 0
        res = " " * (len(s)+1)
        curstring = ""
        c_t = collections.Counter(t)

        while right < len(s):
            curstring += s[right]
            while helper(collections.Counter(curstring), c_t):
                if len(curstring) < len(res):
                    res = curstring
                curstring = curstring[1:]
                left += 1
            right += 1
        return res if len(res) != len(s)+1 else ""


if __name__ == '__main__':
    sol = Solution()
    res = sol.minWindow(s = "ADOBECODEBANC", t = "ABC")
    print(res)
