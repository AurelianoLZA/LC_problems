import collections
import functools
import math
from typing import List
from typing import Optional

'''
给定两个字符串 s 和 t ，判断它们是否是同构的。

如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。

每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。
'''


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def helper(s, t):
            lookup = {}
            if len(s) != len(t):
                return False
            for index in range(len(s)):
                if s[index] not in lookup:
                    lookup[s[index]] = t[index]
                else:
                    if lookup.get(s[index]) != t[index]:
                        return False
            return True
        return helper(s, t) and helper(t, s)

if __name__ == '__main__':
    sol = Solution()
    res = sol.isIsomorphic(s = "foo", t = "bar")
    print(res)
