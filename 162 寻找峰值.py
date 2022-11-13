import collections
import itertools
import math
from typing import List
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 峰值元素是指其值严格大于左右相邻值的元素。
#
# 给你一个整数数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。
#
# 你可以假设 nums[-1] = nums[n] = -∞ 。
#
# 你必须实现时间复杂度为 O(log n) 的算法来解决此问题。
# 输入：nums = [1,2,3,1]
# 输出：2
# 解释：3 是峰值元素，你的函数应该返回其索引 2。

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # 方法一 ： return nums.index(max(nums))

        # Log N =》 二分法
        def get(i: int) -> int:
            if i == -1 or i == len(nums):
                return float('-inf')
            return nums[i]

        left, right  = 0, len(nums)-1
        res = -1
        while(left <= right):
            mid = left + (right-left)//2
            if get(mid-1) < get(mid) > get(mid+1):
                res = mid
                return res

            if get(mid) > get(mid+1):
                right = mid -1
            else:
                left = mid + 1
        return res

sol = Solution()
res = sol.findPeakElement([1,2,3,1])
print(res)
res = sol.findPeakElement([1,2,1,3,5,6,4])
print(res)

