import collections
import functools
import math
from typing import List
from typing import Optional

'''
给你一个字符串 s，如果它是 回文串 ，返回 true ；否则，返回 false 。
输入: s = "A man, a plan, a canal: Panama"
输出：true
解释："amanaplanacanalpanama" 是回文串。

'''


class Solution:
    def isPalindrome(self, s: str) -> bool:

        ls = []
        for ch in s:
            if ch.isalpha():
                ls.append(ch.lower())
        left, right = 0, len(ls)-1
        while left < right:
            if ls[left] != ls[right]:
                return False
            left += 1
            right -= 1
        return True



sol = Solution()
res = sol.isPalindrome(s = "A man, a plan, a canal: Panama")
print(res)
