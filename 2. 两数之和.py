import collections
import functools
import math
from typing import List
from typing import Optional

'''
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
'''


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for index, value in enumerate(nums):
            if (target - value) in dict.keys():
                return [dict.get(target-value), index]
            dict[value] = index
        return []


if __name__ == '__main__':
    sol = Solution()
    res = sol.twoSum(nums = [2,7,11,15], target = 9)
    res = sol.twoSum(nums = [3,2,4], target = 6)
    print(res)
