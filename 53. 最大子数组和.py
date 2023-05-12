import collections
import functools
import math
from typing import List
from typing import Optional

'''
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组 是数组中的一个连续部分。
'''


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        if len(nums) == 1:
            return nums[0]
        left, right = 0, len(nums)-1
        res = 0
        while left <= right:
            res = max(res, sum(nums[left: right+1]))
            if nums[left] < nums[right]:
                left += 1
            else:
                right -=1
        return res


if __name__ == '__main__':
    sol = Solution()
    res = sol.maxSubArray(nums = [-2,1])
    print(res)
