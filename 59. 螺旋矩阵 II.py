import collections
import functools
import math
from typing import List
from typing import Optional

'''
给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。

输入：n = 3
输出：[[1,2,3],[8,9,4],[7,6,5]]
https://leetcode.cn/problems/spiral-matrix-ii/description/?envType=study-plan&id=shu-ju-jie-gou-ji-chu&plan=data-structures&plan_progress=46g37ys

思路 ： 模拟， 每当走到边界 或者 matrix 的值大于0 （说明之前已经走过来）之后就顺时针旋转90度
'''


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        index = 0
        res = [[0 for _ in range(n)] for _ in range(n)]
        print(res)
        startx, starty = 0, 0
        for i in range(n**2):
            res[startx][starty] = i+1
            nextPosX, nextPosY = startx + directions[index][0], starty + directions[index][1]
            if nextPosX < 0 or nextPosX >= n or nextPosY < 0 or nextPosY >= n or res[nextPosX][nextPosY] > 0 :
                index = (index+1) % 4
            startx += directions[index][0]
            starty += directions[index][1]
        return res


sol = Solution()
res = sol.generateMatrix(3)
print(res)
