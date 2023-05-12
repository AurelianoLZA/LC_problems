import collections
import functools
import math
from typing import List
from typing import Optional

'''
给你一个字符串数组 words ，找出并返回 length(words[i]) * length(words[j]) 的最大值，
并且这两个单词不含有公共字母。如果不存在这样的两个单词，返回 0 。
'''


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def helpercheck(word1, word2):
            k1 = collections.Counter(word1).keys()
            k2 = collections.Counter(word2).keys()
            for val1 in k1:
                if val1 in k2:
                    return False
            return True
        maxLength = 0
        words.sort(reverse=True)
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if helpercheck(words[i], words[j]):
                    maxLength = max(maxLength, len(words[j]) * len(words[i]))
        return maxLength


if __name__ == '__main__':
    sol = Solution()
    res = sol.maxProduct(words = ["abcw","baz","foo","bar","xtfn","abcdef"])
    print(res)
