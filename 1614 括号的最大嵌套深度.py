import collections
import functools
import math
from typing import List
from typing import Optional

'''
输入：s = "(1+(2*3)+((8)/4))+1"
输出：3
解释：数字 8 在嵌套的 3 层括号中。
'''


class Solution:
    def maxDepth(self, s: str) -> int:
        maxDepth = 0
        depth = 0
        for ch in s:
            if ch == "(":
                depth +=1
                maxDepth = max(maxDepth, depth)
            elif ch == ")":
                depth -= 1
        return maxDepth


sol = Solution()
res = sol.maxDepth("(1+(2*3)+((8)/4))+1")
print(res)
