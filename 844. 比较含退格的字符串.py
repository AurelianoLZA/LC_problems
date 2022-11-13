import collections
import functools
import math
from typing import List
from typing import Optional

'''
给定 s 和 t 两个字符串，当它们分别被输入到空白的文本编辑器后，如果两者相等，返回 true 。# 代表退格字符。

注意：如果对空文本输入退格字符，文本继续为空。

输入：s = "ab#c", t = "ad#c"
输出：true
解释：s 和 t 都会变成 "ac"。

注意 ： 需要判断ls是否是空的情况：如果ch为# 并且ls是空，需要continue
'''


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def helper(s):
            ls = []
            for ch in s:
                if ch == "#":
                    if ls:
                        ls.pop()
                    else:
                        continue
                else:
                    ls.append(ch)
            return "".join(ls)

        return helper(s) == helper(t)


sol = Solution()
res = sol.backspaceCompare("ab#c", "ad#c")
print(res)
