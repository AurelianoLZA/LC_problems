import collections
import functools
import math
from typing import List
from typing import Optional

'''
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。


'''


class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        for i in range(len(height)):
            for j in range(i, len(height)):
                res = max(res, min(height[i], height[j]) * (j-i))
        return res

    def maxArea2(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        res = 0
        while left < right:
            res = max(res, min(height[left], height[right]) * (right-left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res


if __name__ == '__main__':
    sol = Solution()
    res = sol.maxArea2([1,8,6,2,5,4,8,3,7])
    print(res)
