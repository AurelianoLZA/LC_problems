import collections
import functools
import math
from typing import List
from typing import Optional

'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。
'''


class Solution:
    def isValid(self, s: str) -> bool:
        ls = []
        for ch in s:
            if ch == '(' or ch == '{' or ch =='[':
                ls.append(ch)
            else:
                if ch == ')' and ls[-1] == '(':
                    ls.pop()
                elif ch == ']' and ls[-1] == '[':
                    ls.pop()
                elif ch == '}' and ls[-1] == '{':
                    ls.pop()
                else:
                    return False
        return len(ls)==0

if __name__ == '__main__':
    sol = Solution()
    res = sol.isValid('()')
    print(res)
