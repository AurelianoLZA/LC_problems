import collections
import functools
import math
from typing import List
from typing import Optional

'''
给定一个 row x col 的二维网格地图 grid ，其中：grid[i][j] = 1 表示陆地， grid[i][j] = 0 表示水域。

网格中的格子 水平和垂直 方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。


'''


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def inGrid(grid, i, j):
            return i >=0 and j >=0 and i < len(grid) and j < len(grid[0])
        def dfs(grid, i, j):
            if not inGrid(grid, i, j):
                return 1
            if grid[i][j] == 0:
                return 1
            if grid[i][j] == 2:
                return 0

            grid[i][j] = 2
            return dfs(grid, i-1, j) + dfs(grid, i+1, j) + dfs(grid, i, j-1) + dfs(grid, i, j+1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(grid, i, j)


if __name__ == '__main__':
    sol = Solution()
    res = sol.islandPerimeter(grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])
    print(res)
