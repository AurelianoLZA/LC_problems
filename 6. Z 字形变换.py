import collections
import functools
import math
from typing import List
from typing import Optional

'''
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：
P   A   H   N
A P L S I I G
Y   I   R

输入：s = "PAYPALISHIRING", numRows = 4
输出："PINALSIGYAHRPI"
解释：
P     I    N
A   L S  I G
Y A   H R
P     I

思路：用flag = 1 或者 -1 来控制ls 添加的位置index，当index 到0 或者 numRows-1 时，flag 调转方向
'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ls = [""] * numRows
        flag = -1
        index = 0
        for ch in s:
            if index == 0 or index == numRows-1 :
                flag = - flag
            ls[index] += ch
            index += flag
        return "".join(ls)


sol = Solution()
res = sol.convert("PAYPALISHIRING",3)
print(res)
