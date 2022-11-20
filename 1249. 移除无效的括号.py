import collections
import functools
import math
from typing import List
from typing import Optional

'''
给你一个由 '('、')' 和小写字母组成的字符串 s。

你需要从字符串中删除最少数目的 '(' 或者 ')' （可以删除任意位置的括号)，使得剩下的「括号字符串」有效。

请返回任意一个合法字符串。

有效「括号字符串」应当符合以下 任意一条 要求：

空字符串或只包含小写字母的字符串
可以被写作 AB（A 连接 B）的字符串，其中 A 和 B 都是有效「括号字符串」
可以被写作 (A) 的字符串，其中 A 是一个有效的「括号字符串」
 

示例 1：

输入：s = "lee(t(c)o)de)"
输出："lee(t(c)o)de"
解释："lee(t(co)de)" , "lee(t(c)ode)" 也是一个可行答案。
'''


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        toRemove = []
        ls = []
        for i, ch in enumerate(s):
            if str(ch).isalpha():
                continue
            if ch == "(":
                ls.append(i)
            elif ch == ")":
                if not ls:
                    toRemove.append(i)
                else:
                    ls.pop()
        if ls:
            toRemove += ls
        res = []
        for index in range(len(s)):
            if index not in toRemove:
                res.append(s[index])
        return "".join(res)




        res = []
        for i in range(len(s)):
            if i not in toRemove:
                res.append(s[i])
        return "".join(res) if not ls else ""





sol = Solution()
res = sol.minRemoveToMakeValid("lee(t(c)o)de)")
print(res)
