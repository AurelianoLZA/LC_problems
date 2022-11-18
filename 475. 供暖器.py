import collections
import functools
import math
from typing import List
from typing import Optional

'''
冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。

在加热器的加热半径范围内的每个房屋都可以获得供暖。

现在，给出位于一条水平线上的房屋 houses 和供暖器 heaters 的位置，请你找出并返回可以覆盖所有房屋的最小加热半径。

说明：所有供暖器都遵循你的半径标准，加热的半径也一样。

输入: houses = [1,2,3,4], heaters = [1,4]
输出: 1
解释: 在位置1, 4上有两个供暖器。我们需要将加热半径设为1，这样所有房屋就都能得到供暖。

'''


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        maxRadius = 0
        for house in houses:
            ls = sorted(heaters, key=lambda x : abs(x - house))
            maxRadius = max(maxRadius, abs(ls[0] - house))
        return maxRadius


sol = Solution()
res = sol.findRadius([1,2,3,4],[1,4])
print(res)
