import collections
import functools
import math
from typing import List
from typing import Optional

'''
给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。
'''


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left, right = 0, 0
        res = []
        window = {}
        match = 0
        lookup = collections.Counter(p)
        while right < len(s):
            c_right = s[right]
            #update
            if c_right in lookup.keys():
                window[c_right] = window.get(c_right, 0) +1
                if window[c_right] == lookup[c_right]:
                    match += 1
            right += 1
            while (match == len(lookup)):
                if (right-left) == len(p):
                    res.append(left)
                c_left = s[left]
                if c_left in lookup.keys():
                    window[c_left] -= 1
                    if window[c_left] < lookup[c_left]:
                        match -= 1
                left += 1
        return res






if __name__ == '__main__':
    sol = Solution()
    res = sol.findAnagrams(s = "cbaebabacd", p = "abc")
    print(res)
