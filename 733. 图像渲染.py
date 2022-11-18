import collections
import functools
import math
from typing import List
from typing import Optional

'''
有一幅以 m x n 的二维整数数组表示的图画 image ，其中 image[i][j] 表示该图画的像素值大小。

你也被给予三个整数 sr ,  sc 和 newColor 。你应该从像素 image[sr][sc] 开始对图像进行 上色填充 。

为了完成 上色工作 ，从初始像素开始，记录初始坐标的 上下左右四个方向上 像素值与初始坐标相同的相连像素点，接着再记录这四个方向上符合条件的像素点与他们对应 四个方向上 像素值与初始坐标相同的相连像素点，……，重复该过程。将所有有记录的像素点的颜色值改为 newColor 。

最后返回 经过上色渲染后的图像 。

输入: image = [[1,1,1],[1,1,0],[1,0,1]]，sr = 1, sc = 1, newColor = 2
输出: [[2,2,2],[2,2,0],[2,0,1]]
解析: 在图像的正中间，(坐标(sr,sc)=(1,1)),在路径上所有符合条件的像素点的颜色都被更改成2。
注意，右下角的像素没有更改为2，因为它不是在上下左右四个方向上与初始点相连的像素点。
'''


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        currColor = image[sr][sc]
        def ingrid(i, j):
            return i >= 0 and i < len(image) and j >= 0 and j < len(image[0])
        def dfs(i, j):
            if not ingrid(i,j):
                return
            if image[i][j] != currColor:
                return
            image[i][j] = color
            for new_i, new_j in [(i-1,j), (i+1,j), (i, j-1), (i, j+1)]:
                dfs(new_i, new_j)
        if image[sr][sc] != color:
            dfs(sr, sc)
        return image



sol = Solution()
res = sol.floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2)
print(res)
