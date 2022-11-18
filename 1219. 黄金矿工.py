import collections
import functools
import math
from typing import List
from typing import Optional

'''
你要开发一座金矿，地质勘测学家已经探明了这座金矿中的资源分布，并用大小为 m * n 的网格 grid 进行了标注。每个单元格中的整数就表示这一单元格中的黄金数量；
如果该单元格是空的，那么就是 0。

为了使收益最大化，矿工需要按以下规则来开采黄金：

    每当矿工进入一个单元，就会收集该单元格中的所有黄金。
    矿工每次可以从当前位置向上下左右四个方向走。
    每个单元格只能被开采（进入）一次。
    不得开采（进入）黄金数目为 0 的单元格。
    矿工可以从网格中 任意一个 有黄金的单元格出发或者是停止。
    
输入：grid = [[0,6,0],[5,8,7],[0,9,0]]
输出：24
解释：
[[0,6,0],
 [5,8,7],
 [0,9,0]]
一种收集最多黄金的路线是：9 -> 8 -> 7。

注意 ： 因为可以有多个入口开始进入，每次dfs之后需要把 grid[i][j] 复位成 原来的值

'''


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def ingrid(i, j):
            return i < len(grid) and i >=0 and j >= 0 and j < len(grid[0])
        def dfs(i, j, currSum):
            nonlocal res
            if not ingrid(i, j) or grid[i][j] == 0:
                res = max(res, currSum )
                return

            record = grid[i][j]
            newSum = currSum + grid[i][j]
            grid[i][j] = 0
            for (x,y) in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                dfs(x,y,newSum)
            grid[i][j] = record

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    dfs(i, j, 0)
        return res




sol = Solution()
res = sol.getMaximumGold([[0,6,0],[5,8,7],[0,9,0]])
print(res)
