import collections
import functools
import math
from typing import List
from typing import Optional

'''
实现 pow(x, n) ，即计算 x 的整数 n 次幂函数（即，xn ）。
输入：x = 2.00000, n = 10
输出：1024.00000
'''


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def dfs(val, depth):
            if depth == 1:
                return val
            return dfs(val * x, depth - 1)

        return dfs(x, n)


sol = Solution()
res = sol.myPow(0.00001, 2147483647)
print(res)
