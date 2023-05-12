import collections
import functools
import math
from typing import List
from typing import Optional

'''
给定一个大小为 n 的整数数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。
'''


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = collections.Counter(nums)
        res = []
        for key, val in counter.items():
            if val > int(len(nums)//3):
                res.append(key)
        return res


if __name__ == '__main__':
    sol = Solution()
    res = sol.majorityElement(nums = [3,2,3])
    print(res)
