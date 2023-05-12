import collections
import functools
import math
from typing import List
from typing import Optional

'''
给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。


'''


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        lookup = collections.Counter(nums)
        for key, value in lookup.items():
            if value > len(nums)//2:
                return key
        return -1

if __name__ == '__main__':
    sol = Solution()
    res = sol.majorityElement(nums = [3,2,3])
    print(res)
