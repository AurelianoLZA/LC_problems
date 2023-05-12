    import collections
import functools
import math
from typing import List
from typing import Optional

'''
给你一个字符串 s ，其中包含字母顺序打乱的用英文单词表示的若干数字（0-9）。按 升序 返回原始的数字。

'zero' : z
'one'  : 
'two'  : w
'three': 
'four' : f
'five' : 
'six'  : x
'seven': 
'eight':g
'nine' :
'''


class Solution:
    def originalDigits(self, s: str) -> str:
        c = collections.Counter(s)
        cnt = [0] * 10
        cnt[0] = c["z"]
        cnt[2] = c["w"]
        cnt[4] = c["u"]
        cnt[6] = c["x"]
        cnt[8] = c["g"]

        cnt[3] = c["h"] - cnt[8]
        cnt[5] = c["f"] - cnt[4]
        cnt[7] = c["s"] - cnt[6]

        cnt[1] = c["o"] - cnt[0] - cnt[2] - cnt[4]

        cnt[9] = c["i"] - cnt[5] - cnt[6] - cnt[8]

        return "".join(str(x) * cnt[x] for x in range(10))



if __name__ == '__main__':
    sol = Solution()
    res = sol.originalDigits("s")
    print(res)
