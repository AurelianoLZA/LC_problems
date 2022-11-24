import collections
import functools
import math
from typing import List
from typing import Optional

'''
给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态： 1 即为 活细胞 （live），或 0 即为 死细胞 （dead）。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：

如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。给你 m x n 网格面板 board 的当前状态，返回下一个状态。

 
'''


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def getNum(i, j):
            if i >=0 and j >= 0 and i < len(board) and j < len(board[0]):
                return board[i][j]
            else:
                return 0
        def countHelper(i, j):
            return sum([getNum(i-1, j), getNum(i+1, j), getNum(i,j+1), getNum(i, j-1), getNum(i-1, j-1),
                        getNum(i+1, j-1), getNum(i-1,j+1), getNum(i+1,j+1)])

        res = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if countHelper(i,j) < 2:
                    res[i][j] = 0
                elif 2 <= countHelper(i,j) <= 3 and board[i][j] == 1:
                    res[i][j] = 1
                elif  board[i][j] == 0 and countHelper(i,j) == 3:
                    res[i][j] = 1
                elif countHelper(i,j) > 3:
                    res[i][j] = 0
        print(res)
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = res[i][j]





sol = Solution()
res = sol.gameOfLife(board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]])
res = sol.gameOfLife([[1,1],[1,0]])
print(res)
