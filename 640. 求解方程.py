import collections
import functools
import math
from typing import List
from typing import Optional

'''
求解一个给定的方程，将x以字符串 "x=#value" 的形式返回。该方程仅包含 '+' ， '-' 操作，变量 x 和其对应系数。

如果方程没有解或存在的解不为整数，请返回 "No solution" 。如果方程有无限解，则返回 “Infinite solutions” 。

题目保证，如果方程中只有一个解，则 'x' 的值是一个整数。
输入: equation = "x+5-3+x=6+x-2"
输出: "x=2"

输入: equation = "x=x"
输出: "Infinite solutions"
'''


class Solution:
    def solveEquation(self, equation: str) -> str:
        flag = 1
        num = 0
        coeffx = 0
        index = 0
        while index < len(equation):
            ch = equation[index]
            if ch == "+":
                flag = 1
                index +=1
                continue
            if ch == "-":
                flag = -1
                index += 1
                continue
            if ch == "=":
                flag = 1
                num = -num
                coeffx = -coeffx
            else:
                if ch == "x":
                    coeffx += flag
                else:
                    for j in range(index, len(equation)):
                        if j == len(equation)-1:
                            num += flag * (eval(equation[index:]))
                            break
                        elif equation[j] == "+" or equation[j] == "-" or equation[j] == "=":
                            num += flag * eval("".join(list(equation[index: j])))
                            index  = j
                            break
                        elif equation[j] == "x":
                            coeffx += flag * eval("".join(list(equation[index:j])))
                            index = j
                            flag = 1
                            break
            index += 1
        if coeffx == 0:
            if num == 0:
                return "Infinite Solutions"
            else:
                return "No Solution"
        else:
            res = -num//coeffx
            return "x={}".format(res)






sol = Solution()
res = sol.solveEquation(equation = "x+5-3+x=6+x-2")
res = sol.solveEquation(equation = "2x=x")
res = sol.solveEquation("2x+3x-6x=x+2")
print(res)
