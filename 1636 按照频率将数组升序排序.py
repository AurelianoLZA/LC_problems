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


'''
给你一个整数数组 nums ，请你将数组按照每个值的频率 升序 排序。如果有多个值的频率相同，请你按照数值本身将它们 降序 排序。 

请你返回排序后的数组。

输入：nums = [1,1,2,2,2,3]
输出：[3,1,1,2,2,2]
解释：'3' 频率为 1，'1' 频率为 2，'2' 频率为 3 。
'''


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d = collections.Counter(nums)
        ls = sorted(d.items(), key=lambda x : (x[1], -x[0]))
        res = []
        for key, val in ls:
            for _ in range(val):
                res.append(key)
        return res


sol = Solution()
res = sol.frequencySort([1,1,2,2,2,3])
print(res)
