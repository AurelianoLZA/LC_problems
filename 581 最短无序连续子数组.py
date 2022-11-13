import collections
import functools
import math
from typing import List
from typing import Optional

'''
给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

请你找出符合题意的 最短 子数组，并输出它的长度。

输入：nums = [2,6,4,8,10,9,15]
输出：5
解释：你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。

输入：nums = [1,2,3,4]
输出：0

'''
''' 
思路 ： 将原数组与sort之后的数组对比，找到最长的前缀和后缀
'''


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        copy = sorted(nums[:])
        if sorted(nums) == nums[:]:
            return 0
        left, right = 0, len(nums)-1
        while nums[left] == copy[left]:
                left += 1

        while nums[right] == copy[right]:
                right -= 1
        return right-left + 1



sol = Solution()
res = sol.findUnsortedSubarray([2,6,4,8,10,9,15])
print(res)
