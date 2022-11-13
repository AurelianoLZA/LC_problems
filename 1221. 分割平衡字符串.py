import collections
import functools
import math
from typing import List
from typing import Optional

'''
在一个 平衡字符串 中，'L' 和 'R' 字符的数量是相同的。

给你一个平衡字符串 s，请你将它分割成尽可能多的平衡字符串。

注意：分割得到的每个字符串都必须是平衡字符串，且分割得到的平衡字符串是原平衡字符串的连续子串。

返回可以通过分割得到的平衡字符串的 最大数量 。

输入：s = "RLRRLLRLRL"
输出：4
解释：s 可以分割为 "RL"、"RRLL"、"RL"、"RL" ，每个子字符串中都包含相同数量的 'L' 和 'R' 。

https://leetcode.cn/problems/split-a-string-in-balanced-strings/
'''


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        depth = 0
        cnt = 0
        for ch in s:
            if ch == "L":
                depth += 1
            elif ch == "R":
                depth -= 1
            if depth == 0:
                cnt += 1
        return cnt


sol = Solution()
res = sol.balancedStringSplit("RLRRLLRLRL")
print(res)
