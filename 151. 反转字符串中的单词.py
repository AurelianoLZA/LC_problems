import collections
import functools
import math
import re
from typing import List
from typing import Optional

'''
给你一个字符串 s ，请你反转字符串中 单词 的顺序。

单词 是由非空格字符组成的字符串。s 中使用至少一个空格将字符串中的 单词 分隔开。

返回 单词 顺序颠倒且 单词 之间用单个空格连接的结果字符串。
'''


class Solution:
    def reverseWords(self, s: str) -> str:
        res = re.split("\\s+", s.strip())
        return " ".join(reversed(res))


if __name__ == '__main__':
    sol = Solution()
    res = sol.reverseWords("s   s")
    print(res)
