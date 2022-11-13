import collections
import functools
import math
from typing import List
from typing import Optional

'''
给你一个字符串 s，找到 s 中最长的回文子串。

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        超时 ： 51/140
        '''
        def isPali(s):
            left, right = 0, len(s)-1
            while left <= right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        maxLen = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                subs = "".join(list(s)[i:j+1])
                if isPali(subs) and len(subs) > len(maxLen):
                    maxLen = subs
        return maxLen



sol = Solution()
res = sol.longestPalindrome("babad")
print(res)
