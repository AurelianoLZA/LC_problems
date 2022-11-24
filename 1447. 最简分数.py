import collections
import functools
import math
from typing import List
from typing import Optional

'''
给你一个整数 n ，请你返回所有 0 到 1 之间（不包括 0 和 1）满足分母小于等于  n 的 最简 分数 。分数可以以 任意 顺序返回。

输入：n = 3
输出：["1/2","1/3","2/3"]

通过 gcd，即：最小公倍数，的方法查找分子分母是不是最简，如果gcd==1，说明是最简
'''


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        res = []
        for denom in range(1, n + 1):
            for j in range(1, denom):
                if math.gcd(denom, j) == 1:
                    res.append("/".join([str(j), str(denom)]))
        return res


if __name__ == '__main__':
    sol = Solution()
    res = sol.simplifiedFractions(4)
    print(res)
