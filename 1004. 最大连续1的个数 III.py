import collections
import functools
import math
from typing import List
from typing import Optional

'''
给定一个二进制数组 nums 和一个整数 k，如果可以翻转最多 k 个 0 ，则返回 数组中连续 1 的最大个数 。
输入：nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
输出：10
解释：[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 10。

solution: 题目可以理解为：最长的1连续数组，最多有k个0
'''


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        counter_zero = 0
        res = 0

        while right < len(nums):
            if nums[right] == 0:
                counter_zero += 1
            while(counter_zero > k):
                if nums[left] == 0:
                    counter_zero -= 1
                left += 1
            res = max(res, right-left+1)
            right += 1
        return res




if __name__ == '__main__':
    sol = Solution()
    res = sol.longestOnes(nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3)
    print(res)
