import collections
import functools
import math
from typing import List
from typing import Optional

'''
给出一个字符串 s（仅含有小写英文字母和括号）。

请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。

注意，您的结果中 不应 包含任何括号。

输入：s = "(u(love)i)"
输出："iloveu"
解释：先反转子字符串 "love" ，然后反转整个字符串。
'''


class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == ")":
                temp = []
                while stack and stack[-1] != "(":
                    temp.append(stack.pop())
                stack.pop()
                stack += temp
            else:
                stack.append(ch)
        return "".join(stack)



sol = Solution()
res = sol.reverseParentheses(s = "(u(love)i)")
print(res)
