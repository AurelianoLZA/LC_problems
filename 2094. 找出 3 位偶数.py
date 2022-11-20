import collections
import functools
import math
from typing import List
from typing import Optional

'''
给你一个整数数组 digits ，其中每个元素是一个数字（0 - 9）。数组中可能存在重复元素。

你需要找出 所有 满足下述条件且 互不相同 的整数：

该整数由 digits 中的三个元素按 任意 顺序 依次连接 组成。
该整数不含 前导零
该整数是一个 偶数
例如，给定的 digits 是 [1, 2, 3] ，整数 132 和 312 满足上面列出的全部条件。

将找出的所有互不相同的整数按 递增顺序 排列，并以数组形式返回。
'''


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = set()
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i == j or j == k or i == k:
                        continue
                    val = digits[i] * 100 + digits[j] * 10 + digits[k]
                    if val % 2 == 0 and val >= 100:
                        res.add(val)
        return sorted(list(res))




sol = Solution()
res = sol.findEvenNumbers([2,2,8,8,2])
print(res)
