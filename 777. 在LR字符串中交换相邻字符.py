import collections
import functools
import math
from typing import List
from typing import Optional

'''
在一个由 'L' , 'R' 和 'X' 三个字符组成的字符串（例如"RXXLRXRXL"）中进行移动操作。
一次移动操作指用一个"LX"替换一个"XL"，或者用一个"XR"替换一个"RX"。
现给定起始字符串start和结束字符串end，请编写代码，当且仅当存在一系列移动操作使得start可以转换成end时， 返回True。

输入: start = "RXXLRXRXL", end = "XRLXXRRLX"
输出: True
解释:
我们可以通过以下几步将start转换成end:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX

思路 ： end 的每个R只能在start对应R的右边，end的每个L只能在start对应的左边。
所以在遍历start和end 的时候，
    如果两个char不一样（一个L，一个R），return False
    如果char是R而且i>j, return False
    如果char是L而且i<j, return False 

'''


class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        i, j = 0, 0
        while (i < len(start) or j < len(start)):
            while (i < len(start) and start[i] == "X"):
                i += 1
            while (j < len(end) and end[j] == "X"):
                j += 1
            if i == len(start) or j == len(end):
                return i == j
            if start[i] != end[j]:
                return False
            if start[i] == "R" and i > j:
                return False
            if start[i] == "L" and i < j:
                return False
            i += 1
            j += 1
        return True



sol = Solution()
res = sol.canTransform("RL", "LR")
print(res)
