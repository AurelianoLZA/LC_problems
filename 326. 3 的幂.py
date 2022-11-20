import collections
import functools
import math
from typing import List
from typing import Optional

'''
给定一个整数，写一个函数来判断它是否是 3 的幂次方。如果是，返回 true ；否则，返回 false 。

整数 n 是 3 的幂次方需满足：存在整数 x 使得 n == 3x
输入：n = 27
输出：true
'''


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n > 1:
            if n % 3 == 0:
                n /= 3
            else:
                return False
        return n == 1


sol = Solution()
res = sol.isPowerOfThree(27)
print(res)
