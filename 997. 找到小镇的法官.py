import collections
import functools
import math
from typing import List
from typing import Optional

'''
小镇里有 n 个人，按从 1 到 n 的顺序编号。传言称，这些人中有一个暗地里是小镇法官。

如果小镇法官真的存在，那么：

小镇法官不会信任任何人。
每个人（除了小镇法官）都信任这位小镇法官。
只有一个人同时满足属性 1 和属性 2 。
给你一个数组 trust ，其中 trust[i] = [ai, bi] 表示编号为 ai 的人信任编号为 bi 的人。

如果小镇法官存在并且可以确定他的身份，请返回该法官的编号；否则，返回 -1 。
'''


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inDegree, outDegree = [0] * n, [0] * n
        for item in trust:
            inDegree[item[1]-1] += 1
            outDegree[item[0]-1] += 1
        print(inDegree)
        print(outDegree)
        for i in range(n):
            if inDegree[i] == n-1 and outDegree[i] == 0:
                return i+1

        return -1




sol = Solution()
res = sol.findJudge(n = 3, trust = [[1,3],[2,3]])
print(res)
