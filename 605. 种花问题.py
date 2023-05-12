import collections
import functools
import math
from typing import List
from typing import Optional

'''
假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

给你一个整数数组 flowerbed 表示花坛，由若干 0 和 1 组成，其中 0 表示没种植花，1 表示种植了花。另有一个数 n ，能否在不打破种植规则的情况下种入 n 朵花？能则返回 true ，不能则返回 false 。

输入：flowerbed = [1,0,0,0,1], n = 2
输出：false
'''


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        index = 0
        total = n
        while index < len(flowerbed):
            if flowerbed[index] == 1:
                index += 2
                continue
            else:
                if index == len(flowerbed)-2:
                    if flowerbed[len(flowerbed)-1] == 1 :
                        break
                total -= 1
                index += 2
        return total == 0


if __name__ == '__main__':
    sol = Solution()
    res = sol.canPlaceFlowers(flowerbed = [1,0,0,0,0,1], n = 2)
    print(res)
