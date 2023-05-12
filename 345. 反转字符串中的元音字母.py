import collections
import functools
import math
from typing import List
from typing import Optional

'''
给你一个字符串 s ，仅反转字符串中的所有元音字母，并返回结果字符串。

元音字母包括 'a'、'e'、'i'、'o'、'u'，且可能以大小写两种形式出现不止一次
'''


class Solution:
    def reverseVowels(self, s: str) -> str:
        aeiou = ('a', 'e', 'i', 'o', 'u')
        ls = []
        for ch in s:
            if ch.lower() in aeiou:
                ls.append(ch)
        ls.reverse()
        strls = []
        for ch in s:
            if ch.lower() in aeiou:
                strls.append(ls.pop(0))
            else:
                strls.append(ch)
        return "".join(strls)



if __name__ == '__main__':
    sol = Solution()
    res = sol.reverseVowels("leetcode")
    print(res)
