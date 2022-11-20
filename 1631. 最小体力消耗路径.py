import collections
import functools
import math
from typing import List
from typing import Optional

'''
你准备参加一场远足活动。给你一个二维 rows x columns 的地图 heights ，其中 heights[row][col] 表示格子 (row, col) 的高度。一开始你在最左上角的格子 (0, 0) ，且你希望去最右下角的格子 (rows-1, columns-1) （注意下标从 0 开始编号）。你每次可以往 上，下，左，右 四个方向之一移动，你想要找到耗费 体力 最小的一条路径。

一条路径耗费的 体力值 是路径上相邻格子之间 高度差绝对值 的 最大值 决定的。

请你返回从左上角走到右下角的最小 体力消耗值 。

输入：heights = [[1,2,2],[3,8,2],[5,3,5]]
输出：2
解释：路径 [1,3,5,3,5] 连续格子的差值绝对值最大为 2 。
这条路径比路径 [1,2,2,2,5] 更优，因为另一条路径差值最大值为 3 。
'''


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        res = []
        def ingrid(i, j):
            return i >= 0 and j >= 0 and i < len(heights) and j < len(heights[0])
        def dfs(i, j, path):
            nonlocal res
            if not ingrid(i, j):
                return

            if i == len(heights)-1 and j == len(heights[0])-1:
                path += [heights[i][j]]
                res.append(path)
                return
            dfs(i+1, j, path + [heights[i][j]])
            dfs(i, j+1, path + [heights[i][j]])


        dfs(0,0,[])
        minMax = 10000000000
        for path in res:
            print(path)
            Max = 0
            for i in range(1, len(path)):
                Max = max(Max, path[i]-path[i-1])
            minMax = min(minMax, Max)
        return minMax




sol = Solution()
res = sol.minimumEffortPath(heights = [[4,3,4,10,5,5,9,2],[10,8,2,10,9,7,5,6],[5,8,10,10,10,7,4,2],[5,1,3,1,1,3,1,9],[6,4,10,6,10,9,4,6]])
print(res)
