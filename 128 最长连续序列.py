import collections
import functools
import math
from typing import List
from typing import Optional

'''
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
'''

''' 
注意：【0，1，1，2】 应该返回3 而不是4，所以我们要计算的是nums[right]-nums[left]+1 的最大值
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, 0
        maxSize = 0
        while right < len(nums):
            while (right < len(nums) - 1 and (nums[right + 1] == nums[right] + 1 or nums[right] == nums[right + 1])):
                right += 1
            maxSize = max(maxSize, nums[right] - nums[left] + 1)
            left = right + 1
            right += 1
        return maxSize



sol = Solution()
res = sol.longestConsecutive([100,4,200,1,3,2])
print(res)
