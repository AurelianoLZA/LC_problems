import collections
import functools
import math
from typing import List
from typing import Optional

'''
给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex 行。

在「杨辉三角」中，每个数是它左上方和右上方的数的和。

输入: rowIndex = 3
输出: [1,3,3,1]
'''


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0 :
            return [1]
        if rowIndex == 1:
            return [1,1]
        ls = [1,1]
        for row in range(2, rowIndex+1):
            temp = []
            for i in range(len(ls)-1):
                temp.append(ls[i] + ls[i+1])
            ls = [1] + temp + [1]
        return ls





sol = Solution()
res = sol.getRow(4)
print(res)
