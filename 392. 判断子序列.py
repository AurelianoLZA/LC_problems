import collections
import functools
import math
from typing import List
from typing import Optional

'''
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

输入：s = "abc", t = "ahbgdc"
输出：true
'''


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        index = 0
        for char in t:
            if index < len(s) and char == s[index]:
                index += 1
        return index == len(s)


sol = Solution()
res = sol.isSubsequence(s = "abc", t = "ahbgdc")
print(res)
