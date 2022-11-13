import collections
import itertools
import math
from typing import List
from typing import Optional


'''
给你两个下标从 0 开始的字符串 s 和 target 。你可以从 s 取出一些字符并将其重排，得到若干新的字符串。

从 s 中取出字符并重新排列，返回可以形成 target 的 最大 副本数。
'''


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        d_s = collections.Counter(s)
        d_t = collections.Counter(target)
        minNeed = 10**23
        for ch in target:
            minNeed = min(minNeed, d_s[ch] // d_t[ch])
        return minNeed



sol = Solution()
res = sol.rearrangeCharacters("ilovecodingonleetcode","code")
print(res)
