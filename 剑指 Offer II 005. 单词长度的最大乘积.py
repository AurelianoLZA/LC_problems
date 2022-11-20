import collections
import functools
import math
from typing import List
from typing import Optional

'''
给定一个字符串数组 words，请计算当两个字符串 words[i] 和 words[j] 不包含相同字符时，它们长度的乘积的最大值。
假设字符串中只包含英语的小写字母。如果没有不包含相同字符的一对字符串，返回 0。

输入: words = ["abcw","baz","foo","bar","fxyz","abcdef"]
输出: 16 
解释: 这两个单词为 "abcw", "fxyz"。它们不包含相同字符，且长度的乘积最大。
'''


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        res = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if set(words[i]) & set(words[j]) == set():
                    res = max(res, len(words[i]) * len(words[j]))
        return res



sol = Solution()
res = sol.maxProduct(words = ["abcw","baz","foo","bar","fxyz","abcdef"])
print(res)
