import collections
import functools
import math
from typing import List
from typing import Optional

'''
给你两个整数数组 nums1 和 nums2 ，请你以数组形式返回两数组的交集。
返回结果中每个元素出现的次数，应与元素在两个数组中都出现的次数一致（如果出现次数不一致，则考虑取较小值）。
可以不考虑输出结果的顺序。

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]

'''


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        c1, c2 = collections.Counter(nums1), collections.Counter(nums2)
        for key in c1.keys():
            if key in c2.keys():
                for _ in range(min(c1[key], c2[key])):
                    res.append(key)
        return res


sol = Solution()
res = sol.intersect(nums1 = [1,2,2,1], nums2 = [2,2])
print(res)
