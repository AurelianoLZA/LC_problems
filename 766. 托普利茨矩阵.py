import collections
import functools
import math
from typing import List
from typing import Optional

'''
给你一个 m x n 的矩阵 matrix 。如果这个矩阵是托普利茨矩阵，返回 true ；否则，返回 false 。

如果矩阵上每一条由左上到右下的对角线上的元素都相同，那么这个矩阵是 托普利茨矩阵 

输入：matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
输出：true
解释：
在上述矩阵中, 其对角线为: 
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]"。 
各条对角线上的所有元素均相同, 因此答案是 True 。
'''


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix)):
            initialval = matrix[i][0]
            y = 0
            x = i
            while x < len(matrix) and y < len(matrix[0]):
                if matrix[x][y] != initialval:
                    return False
                x += 1
                y += 1
        for j in range(len(matrix[0])):
            initialval = matrix[0][j]
            x = 0
            y = j
            while x < len(matrix) and y < len(matrix[0]):
                if matrix[x][y] != initialval:
                    return False
                x += 1
                y += 1
        return True




sol = Solution()
res = sol.isToeplitzMatrix([[1,2],[2,2]])
print(res)
