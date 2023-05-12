import collections
import functools
import math
from typing import List
from typing import Optional

'''
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。
'''


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def ingrid(grid, i, j):
            return i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0])

        def dfs(grid, i, j):
            if not ingrid(grid, i, j):
                return
            if grid[i][j] == '2' or grid[i][j] == '0':
                return
            grid[i][j] = '2'
            dfs(grid, i+1, j)
            dfs(grid, i-1, j)
            dfs(grid, i, j+1)
            dfs(grid, i, j-1)

        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    cnt += 1
                    dfs(grid, i, j)
        return cnt


if __name__ == '__main__':
    sol = Solution()
    res = sol.numIslands(grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
])
    print(res)
