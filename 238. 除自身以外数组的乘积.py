import collections
import functools
import math
from typing import List
from typing import Optional

'''
给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。

题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。

请不要使用除法，且在 O(n) 时间复杂度内完成此题。

输入: nums = [1,2,3,4]
输出: [24,12,8,6]

用类似前缀后缀的方法，先计算出 i 之前的所有乘积 以及 i 之后的所有乘积L，R ： 
L[i] = L[i-1] * nums[i-1]
R[i] = R[i+1] * nums[i+1]
res[i] = L[i] * R[i] 
'''


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res, l, r = [0] * len(nums), [0] * len(nums), [0] * len(nums)
        l[0] = 1
        r[-1] = 1
        for i in range(1, len(nums)):
            l[i] = l[i-1] * nums[i-1]
        for j in range(len(nums)-2, -1, -1):
            r[j] = r[j+1] * nums[j+1]
        for k in range(len(nums)):
            res[k] = l[k] * r[k]
        return res




sol = Solution()
res = sol.productExceptSelf([4,5,1,8,2])
print(res)
