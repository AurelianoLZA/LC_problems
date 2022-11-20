import collections
import functools
import math
from typing import List
from typing import Optional

'''
给你一个 升序排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，
返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。

输入：nums = [1,1,2]
输出：2, nums = [1,2,_]
解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。
'''


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right = 0, 0
        for right in range(len(nums)):
            if nums[left] != nums[right]:
                nums[left+1] = nums[right]
                left += 1
        return left+1


sol = Solution()
res = sol.removeDuplicates([1,1,2])
print(res)
