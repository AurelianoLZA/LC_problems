import collections
import functools
import math
from typing import List
from typing import Optional

'''
给你一个整数数组 nums 和一个整数 k ，请你返回子数组内所有元素的乘积严格小于 k 的连续子数组的数目。
'''


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # 超时
        # def mult(arr):
        #     res = 1
        #     for val in arr:
        #         res *= val
        #     return res
        # counter = 0
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         if mult(nums[i:j+1]) < k:
        #             counter += 1
        # return counter

        # sliding window
        left, right = 0, 0
        res = 0
        curval  = 1
        while right < len(nums):
            curval *= nums[right]
            while(curval >= k):
                curval /= nums[left]
                left += 1
            res += right-left+1
            right += 1
        return res


if __name__ == '__main__':
    sol = Solution()
    res = sol.numSubarrayProductLessThanK(nums = [10,5,2,6], k = 100)
    print(res)
