import collections
import functools
import math
from typing import List
from typing import Optional

'''
给定一个整数 num，将其转化为 7 进制，并以字符串形式输出。
输入: num = 100
输出: "202"
输入: num = -7
输出: "-10"
'''


class Solution:
    def convertToBase7(self, num: int) -> str:
        negative = False
        if num < 0:
            num = -num
            negative = True
        ls = []
        while num > 0:
            a, b = divmod(num, 7)
            ls.append(str(b))
            num = a
        print(ls)
        return "".join(reversed(ls)) if not negative else "-" + "".join(reversed(ls))


sol = Solution()
res = sol.convertToBase7(-100)
print(res)
