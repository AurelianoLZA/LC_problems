import collections
import functools
import math
from typing import List
from typing import Optional

'''
给定一个二进制数组 nums ， 计算其中最大连续 1 的个数。


'''


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left, right = 0, 0
        res = 0
        while (left < len(nums) and right < len(nums)):
            if nums[left] == 1:
                while(right < len(nums) and nums[right] == 1):
                    right += 1
                res = max(res, right-left)
                left = right
            else:
                left += 1
                right += 1
        return res

if __name__ == '__main__':
    sol = Solution()
    res = sol.findMaxConsecutiveOnes(nums = [1,1,0,1,1,1])
    print(res)
