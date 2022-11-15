import collections
import functools
import math
from typing import List
from typing import Optional

'''
给你一个整数数组 nums，和一个整数 k 。

对于每个下标 i（0 <= i < nums.length），将 nums[i] 变成 nums[i] + k 或 nums[i] - k 。

nums 的 分数 是 nums 中最大元素和最小元素的差值。

在更改每个下标对应的值之后，返回 nums 的最小 分数 。

输入：nums = [1,3,6], k = 3
输出：3
解释：将数组变为 [4, 6, 3] 。分数 = max(nums) - min(nums) = 6 - 3 = 3 。

'''


class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        ls = [0] * len(nums)
        nums.sort()
        for i in range(1, len(nums)-1):
            case1 = nums[i]



# sol = Solution()
# res = sol.
# print(res)
