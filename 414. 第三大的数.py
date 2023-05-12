import collections
import functools
import math
from typing import List
from typing import Optional

'''
给你一个非空数组，返回此数组中 第三大的数 。如果不存在，则返回数组中最大的数。


'''


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        if len(nums) > 2:
            return sorted(nums, reverse=True)[2]
        return max(nums)


if __name__ == '__main__':
    sol = Solution()
    res = sol.thirdMax([3,2,1])
    print(res)
