import collections
import functools
import math
from typing import List
from typing import Optional

'''
给你一个字符串 columnTitle ，表示 Excel 表格中的列名称。返回 该列名称对应的列序号 。

例如：

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
输入: columnTitle = "AB"
输出: 28
'''


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        exp = 0
        res = 0
        for ch in columnTitle[::-1]:
            res += (ord(ch.lower())-ord('a')+1) * 26**exp
            exp += 1
        return res




sol = Solution()
res = sol.titleToNumber("ZY")
print(res)
