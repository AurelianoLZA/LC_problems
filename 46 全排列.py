import collections
import itertools
import math
from typing import List
from typing import Optional

'''
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
'''


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(index):
            if index == len(nums):
                res.append(nums)
            for i in range(index, len(nums)):
                nums[i], nums[index] = nums[index], nums[i]
                backtrack(index+1)
                nums[i], nums[index] = nums[index], nums[i]
        res = []
        backtrack(0)
        return res



