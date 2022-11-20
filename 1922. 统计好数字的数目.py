import collections
import functools
import math
from typing import List
from typing import Optional

'''
我们称一个数字字符串是 好数字 当它满足（下标从 0 开始）偶数 下标处的数字为 偶数 且 奇数 下标处的数字为 质数 （2，3，5 或 7）。

比方说，"2582" 是好数字，因为偶数下标处的数字（2 和 8）是偶数且奇数下标处的数字（5 和 2）为质数。但 "3245" 不是 好数字，因为 3 在偶数下标处但不是偶数。
给你一个整数 n ，请你返回长度为 n 且为好数字的数字字符串 总数 。由于答案可能会很大，请你将它对 109 + 7 取余后返回 。

一个 数字字符串 是每一位都由 0 到 9 组成的字符串，且可能包含前导 0 。

 输入：n = 1
输出：5
解释：长度为 1 的好数字包括 "0"，"2"，"4"，"6"，"8" 。
'''


class Solution:
    def countGoodNumbers(self, n: int) -> int:
        even = 0
        odd = 0
        if n%2 == 0:
            even, odd = n//2, n//2
        else:
            even = n//2+1
            odd = n//2
        return ((5**even) * (4 **odd))%(10**9+7)



sol = Solution()
res = sol.countGoodNumbers(50)
print(res)
