import collections
import functools
import math
from typing import List
from typing import Optional

'''
给你一个整数数组 nums 和一个整数 k ，判断数组中是否存在两个 不同的索引 i 和 j ，满足 nums[i] == nums[j] 且 abs(i - j) <= k 。如果存在，返回 true ；否则，返回 false 。
'''


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        lookup = {}
        for index, value in enumerate(nums):
            if value in lookup.keys() and abs(index - lookup.get(value)) <= k:
                return  True
            lookup[value] = index
        return False



if __name__ == '__main__':
    sol = Solution()
    res = sol.containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2)
    print(res)
