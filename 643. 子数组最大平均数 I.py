import collections
import functools
import math
from typing import List
from typing import Optional

'''
给你一个由 n 个元素组成的整数数组 nums 和一个整数 k 。

请你找出平均数最大且 长度为 k 的连续子数组，并输出该最大平均数。
'''


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        totalSum = sum(nums[:k])
        maxVal = totalSum

        for i in range(k , len(nums)):
            totalSum = totalSum - nums[i-k] + nums[i]
            maxVal = max(maxVal, totalSum)
        return maxVal/k


if __name__ == '__main__':
    sol = Solution()
    res = sol.findMaxAverage(nums = [0,1,1,3,3], k = 4)
    print(res)
