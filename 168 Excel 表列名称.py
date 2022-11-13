import collections
import itertools
import math
from typing import List
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

''' 
# 给你一个整数 columnNumber ，返回它在 Excel 表中相对应的列名称。
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28
# 输入：columnNumber = 701
# 输出："ZY"
'''

'''
我们需要在每次运算前先对columnNumber-1, 
因为我们常规的mod操作是在【0，x】的基础上，而这次是从1开始
'''

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        table = {}
        for i in range(1, 27):
            table[i-1] = chr(96+i).upper()
        ls = []
        while columnNumber > 0 :
            columnNumber -= 1 # 重点！
            a,b = divmod(columnNumber, 26)
            ls.append(table[b])
            columnNumber = a
        return "".join(reversed(ls))

sol = Solution()
res = sol.convertToTitle(701)
print(res)
res = sol.convertToTitle(2147483647)
print(res)


