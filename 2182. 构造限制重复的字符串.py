import collections
import functools
import math
from typing import List
from typing import Optional

'''
给你一个字符串 s 和一个整数 repeatLimit ，用 s 中的字符构造一个新字符串 repeatLimitedString ，使任何字母 连续 出现的次数都不超过 repeatLimit 次。你不必使用 s 中的全部字符。

返回 字典序最大的 repeatLimitedString 。

如果在字符串 a 和 b 不同的第一个位置，字符串 a 中的字母在字母表中出现时间比字符串 b 对应的字母晚，则认为字符串 a 比字符串 b 字典序更大 。如果字符串中前 min(a.length, b.length) 个字符都相同，那么较长的字符串字典序更大。

输入：s = "cczazcc", repeatLimit = 3
输出："zzcccac"
解释：使用 s 中的所有字符来构造 repeatLimitedString "zzcccac"。
字母 'a' 连续出现至多 1 次。
字母 'c' 连续出现至多 3 次。
字母 'z' 连续出现至多 2 次。
因此，没有字母连续出现超过 repeatLimit 次，字符串是一个有效的 repeatLimitedString 。
该字符串是字典序最大的 repeatLimitedString ，所以返回 "zzcccac" 。
注意，尽管 "zzcccca" 字典序更大，但字母 'c' 连续出现超过 3 次，所以它不是一个有效的 repeatLimitedString 。
'''


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        # sortedstr = (sorted(s, reverse=True))
        repo = list(s)

        res = []
        while repo:
            c = collections.Counter(repo)
            repo.sort(reverse=True)
            temp = []
            while res and repo[0] == res[-1]:
                temp.append(repo.pop(0))

            for _ in range(min((c[repo[0]]), 3)):
                res.append(repo.pop(0))
            repo += temp
        return "".join(res)



sol = Solution()
res = sol.repeatLimitedString(s = "cczazcc", repeatLimit = 3)
res = sol.repeatLimitedString(s = "aababab", repeatLimit = 2)
print(res)
