import collections
import functools
import math
from typing import List
from typing import Optional

'''
给你一个字符串 s ，字符串的「能量」定义为：只包含一种字符的最长非空子字符串的长度。

请你返回字符串 s 的 能量。

输入：s = "leetcode"
输出：2
解释：子字符串 "ee" 长度为 2 ，只包含字符 'e' 。
'''


class Solution:
    def maxPower(self, s: str) -> int:
        left, right = 0, 0
        maxCnt = 0
        while right < len(s):
            while right+1 < len(s) and  s[left] == s[right+1]:
                right += 1
                continue
            maxCnt = max(maxCnt, right - left + 1)
            left += 1
            right = left

        return maxCnt

if __name__ == '__main__':


    sol = Solution()
    res = sol.maxPower("leetcode")
    res = sol.maxPower("abbcccddddeeeeedcba")
    print(res)
