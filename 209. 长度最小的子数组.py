import collections
import functools
import math
from typing import List
from typing import Optional

'''
                                            滑动窗口
给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。
'''


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        minLength = len(nums)+1
        curSum = 0
        left, right = 0, 0
        while(right < len(nums) and left < len(nums)):
            curSum += nums[right]
            while(curSum >= target):
                minLength = min(minLength, right-left+1)
                curSum -= nums[left]
                left += 1
            right += 1
        return minLength



if __name__ == '__main__':
    sol = Solution()
    res = sol.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3])
    print(res)
