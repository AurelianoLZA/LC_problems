import collections
import functools
import math
from typing import List
from typing import Optional

'''
给你一个整数 n ，对于 0 <= i <= n 中的每个 i ，计算其二进制表示中 1 的个数 ，返回一个长度为 n + 1 的数组 ans 作为答案。

输入：n = 2
输出：[0,1,1]
解释：
0 --> 0
1 --> 1
2 --> 10
'''


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            res.append(collections.Counter(bin(i)[2:])["1"])
        return res


sol = Solution()
res = sol.countBits(2)
print(res)
