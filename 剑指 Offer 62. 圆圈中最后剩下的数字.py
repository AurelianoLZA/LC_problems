import collections
import functools
import math
from typing import List
from typing import Optional

'''
0,1,···,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字（删除后从下一个数字开始计数）。求出这个圆圈里剩下的最后一个数字。

例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。

输入: n = 5, m = 3
输出: 3

'''
'''  
 -->  约瑟夫环 <--
f(n) = (f(n-1) + m) % i
f(n) : 上一次次的index
f(n-1) : 这次的index
m : 隔几个（题目中为3）
i : 上一次的数组大小
'''

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        res = 0
        for i in range(2, n+1):
            res = (res + m) % i
        return res



sol = Solution()
res = sol.lastRemaining(5,3)
print(res)
