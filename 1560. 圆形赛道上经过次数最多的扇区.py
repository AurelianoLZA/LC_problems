import collections
import functools
import math
from typing import List
from typing import Optional

'''
给你一个整数 n 和一个整数数组 rounds 。有一条圆形赛道由 n 个扇区组成，扇区编号从 1 到 n 。现将在这条赛道上举办一场马拉松比赛，该马拉松全程由 m 个阶段组成。其中，第 i 个阶段将会从扇区 rounds[i - 1] 开始，到扇区 rounds[i] 结束。举例来说，第 1 阶段从 rounds[0] 开始，到 rounds[1] 结束。

请你以数组形式返回经过次数最多的那几个扇区，按扇区编号 升序 排列。

思路 ： 只看起始点和结束点，之间的差的片段就是结果。
如果结束点在起始点后面，直接返回之间的所有结点的list
如果结束点在起始点的前面，答案是从结束点到n，然后从1 到起始点
'''


class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        startIndex = rounds[0]
        endIndex = rounds[-1]
        if startIndex <= endIndex:
            return list(range(startIndex, endIndex+1))
        else:
            ls = []
            ls += list(range(startIndex, n+1))
            ls += list(range(1, endIndex+1))
            return sorted(ls)






sol = Solution()
# res = sol.mostVisited(4, [1,3,1,2])
# res = sol.mostVisited(n = 2, rounds = [2,1,2,1,2,1,2,1,2])
res = sol.mostVisited(n = 7, rounds = [1,3,5,7])
print(res)
