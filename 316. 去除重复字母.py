import collections
import functools
import math
from typing import List
from typing import Optional

'''
给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。
示例 1：

输入：s = "bcabc"
输出："abc"
示例 2：

输入：s = "cbacdcbc"
输出："acdb"

'''


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            ch = s[i]
            if not stack:
                stack.append(ch)
                continue
            if ch in stack:
                continue

            elif ch < stack[-1]:
                while stack and ch < stack[-1]:
                    if stack[-1] in s[i + 1:]:
                        stack.pop()
                        # stack.append(ch)
                        # i -= 1
                    else:
                        stack.append(ch)
            else:
                stack.append(ch)
        return "".join(stack)



sol = Solution()
res = sol.removeDuplicateLetters(s = "bcabc")
print(res)
