import collections
import functools
import math
from typing import List
from typing import Optional

'''
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        lookup = set()
        maxLength = 0
        curLength = 0
        left = 0
        for i in range(len(s)):
            curLength += 1
            while(s[i] in lookup):
                lookup.remove(s[left])
                curLength -= 1
                left += 1
            maxLength = max(maxLength, i-left+1)
            lookup.add(s[i])
        return maxLength




if __name__ == '__main__':
    sol = Solution()
    res = sol.lengthOfLongestSubstring(s = "abcabcbb")
    print(res)
