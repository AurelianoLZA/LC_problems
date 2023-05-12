import collections
import functools
import math
from typing import List
from typing import Optional

'''
给你一个整数数组 nums 。如果任一值在数组中出现 至少两次 ，返回 true ；如果数组中每个元素互不相同，返回 false 。
'''


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        lookup = collections.Counter(nums)
        for key, val in lookup.items():
            if val >= 2 :
                return True
        return False


if __name__ == '__main__':
    sol = Solution()
    res = sol.containsDuplicate([1,2,3,1])
    print(res)
