import collections
import functools
import math
from typing import List
from typing import Optional

'''
给定一个字符串 s 和一个整数 k，从字符串开头算起，每计数至 2k 个字符，就反转这 2k 字符中的前 k 个字符。

如果剩余字符少于 k 个，则将剩余字符全部反转。
如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。

输入：s = "abcdefg", k = 2
输出："bacdfeg"
'''


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ls = list(s)
        for i in range(0, len(ls), 2 * k):
            ls[i:i+k] = reversed(ls[i:i+k])
        return "".join(ls)



if __name__ == '__main__':
    sol = Solution()
    res = sol.reverseStr(s = "abcdefg", k = 2)
    print(res)
