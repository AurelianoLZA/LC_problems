import collections
import functools
import math
from typing import List
from typing import Optional

'''
给你一个整数数组 nums ，判断这个数组中是否存在长度为 3 的递增子序列。

如果存在这样的三元组下标 (i, j, k) 且满足 i < j < k ，使得 nums[i] < nums[j] < nums[k] ，返回 true ；否则，返回 false 。

输入：nums = [1,2,3,4,5]
输出：true
解释：任何 i < j < k 的三元组都满足题意
'''


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        leftLs = [False] * len(nums)
        rightLS = [False] * len(nums)
        leftmin = 10**23
        for i in range(len(nums)):
            leftLs[i] = leftmin  < nums[i]
            leftmin = min(leftmin, nums[i])
        rightmax = -1
        for j in range(len(nums)-1, -1, -1):
            rightLS[j] = rightmax > nums[j]
            rightmax = max(rightmax, nums[j])
        for k in range(len(nums)):
            if leftLs[k] and rightLS[k]:
                return True
        return False



        ' 超时 74 / 77 '

        # leftLs = [False] * len(nums)
        # rightLS = [False] * len(nums)
        # leftLs[0], rightLS[len(nums)-1] = False, False
        # for i in range(1, len(nums)):
        #     leftLs[i] = True in list(map(lambda x : x < nums[i], nums[:i]))
        # for j in range(len(nums)-1):
        #     rightLS[j] = True in list(map(lambda x : x > nums[j], nums[j+1:]))
        # print(leftLs)
        # print(rightLS)
        # for k in range(len(nums)):
        #     if leftLs[k] and rightLS[k]:
        #         return True
        # return False



sol = Solution()
res = sol.increasingTriplet([2,1,5,0,4,6])
print(res)
