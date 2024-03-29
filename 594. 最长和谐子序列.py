import collections
import functools
import math
from typing import List
from typing import Optional

'''
和谐数组是指一个数组里元素的最大值和最小值之间的差别 正好是 1 。

现在，给你一个整数数组 nums ，请你在所有可能的子序列中找到最长的和谐子序列的长度。

数组的子序列是一个由数组派生出来的序列，它可以通过删除一些元素或不删除元素、且不改变其余元素的顺序而得到。


'''


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums = sorted(nums)
        maxLength = 0
        left = 0
        while left < len(nums):
            base = nums[left]
            right = left + 1
            while(right < len(nums) and nums[right] == base + 1):
                right += 1
            maxLength = max(maxLength, right-left+1)
            left += 1

        return maxLength


if __name__ == '__main__':
    sol = Solution()
    res = sol.findLHS(nums = [1,3,2,2,5,2,3,7])
    print(res)
