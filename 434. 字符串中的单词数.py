import collections
import functools
import math
from typing import List
from typing import Optional

'''
统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。

请注意，你可以假定字符串里不包括任何不可打印的字符。
'''


class Solution:
    def countSegments(self, s: str) -> int:
        if s == "":
            return 0
        ls = list(filter(lambda x: x != "", s.strip().split(" ")))
        print(ls)
        return len(ls)

if __name__ == '__main__':
    sol = Solution()
    res = sol.countSegments("                ")
    print(res)
