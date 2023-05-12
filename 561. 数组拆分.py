import collections
import functools
import math
from typing import List
from typing import Optional

'''
给定长度为 2n 的整数数组 nums ，你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从 1 到 n 的 min(ai, bi) 总和最大。

返回该 最大总和 。
'''


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        s = 0
        ls = sorted(nums)
        for i in range(0, len(nums), 2):
            s += ls[i]
        return s


if __name__ == '__main__':
    sol = Solution()
    res = sol.arrayPairSum(nums = [1,4,3,2])
    print(res)
