import collections
import functools
import math
from typing import List
from typing import Optional

'''
给定一个字符串 s ，找到 它的第一个不重复的字符，并返回它的索引 。如果不存在，则返回 -1 。

 
'''


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = collections.Counter(s)
        for ch in s:
            if counter.get(ch) == 1:
                return s.index(ch)
        return -1


if __name__ == '__main__':
    sol = Solution()
    res = sol.firstUniqChar("loveleetcode")
    print(res)
