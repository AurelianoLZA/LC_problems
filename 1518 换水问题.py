import collections
import functools
import math
from typing import List
from typing import Optional

'''
超市正在促销，你可以用 numExchange 个空水瓶从超市兑换一瓶水。最开始，你一共购入了 numBottles 瓶水。

如果喝掉了水瓶中的水，那么水瓶就会变成空的。

给你两个整数 numBottles 和 numExchange ，返回你 最多 可以喝到多少瓶水。

输入：numBottles = 9, numExchange = 3
输出：13
解释：你可以用 3 个空瓶兑换 1 瓶水。
所以最多能喝到 9 + 3 + 1 = 13 瓶水。

numBottles = 15, numExchange = 4
输出：19
解释：你可以用 4 个空瓶兑换 1 瓶水。
所以最多能喝到 15 + 3 + 1 = 19 瓶水。

https://leetcode.cn/problems/water-bottles/description/

'''


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        water, bottles  = numBottles, numBottles
        res = water
        while numBottles >= numExchange:
            numBottles -= numExchange
            numBottles += 1
            res += 1
        return res




sol = Solution()
res = sol.numWaterBottles(9, 3)
print(res)
