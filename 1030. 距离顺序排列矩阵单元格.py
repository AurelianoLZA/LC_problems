import collections
import functools
import math
from typing import List
from typing import Optional

'''
给定四个整数 rows ,   cols ,  rCenter 和 cCenter 。有一个 rows x cols 的矩阵，你在单元格上的坐标是 (rCenter, cCenter) 。

返回矩阵中的所有单元格的坐标，并按与 (rCenter, cCenter) 的 距离 从最小到最大的顺序排。你可以按 任何 满足此条件的顺序返回答案。

单元格(r1, c1) 和 (r2, c2) 之间的距离为|r1 - r2| + |c1 - c2|。

输入：rows = 2, cols = 2, rCenter = 0, cCenter = 1
输出：[[0,1],[0,0],[1,1],[1,0]]
解释：从 (r0, c0) 到其他单元格的距离为：[0,1,1,2]
[[0,1],[1,1],[0,0],[1,0]] 也会被视作正确答案。
'''


class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        ls = []
        for i in range(rows):
            for j in range(cols):
                ls.append([i,j])
        ls.sort(key=lambda x : abs(x[0]-rCenter) + abs(x[1]-cCenter))
        return ls




sol = Solution()
res = sol.allCellsDistOrder(rows = 1, cols = 2, rCenter = 0, cCenter = 0)
print(res)
