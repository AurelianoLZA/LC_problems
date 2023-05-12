import collections
import functools
import math
from typing import List
from typing import Optional

'''
给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。

换句话说，s1 的排列之一是 s2 的 子串 。
输入：s1 = "ab" s2 = "eidbaooo"
输出：true
解释：s2 包含 s1 的排列之一 ("ba").
'''


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        for i in range(len(s2)-len(s1)+1):
            if sorted(s2[i:i+len(s1)]) == sorted(s1):
                return True
        return False

    def checkInclusion2(self, s1: str, s2: str) -> bool:
        match = 0
        left, right = 0, 0
        window = {}
        needs  = collections.Counter(s1)
        while right < len(s2):
            c_right = s2[right]
            # update
            if c_right in needs.keys():
                window[c_right] = window.get(c_right, 0) + 1
                if window[c_right] == needs.get(c_right):
                    match += 1

            while (right-left+1 >= len(s1)):
                if (match == len(needs)):
                    return True
                c_left = s2[left]
                # update
                if c_left in needs.keys():
                    if window[c_left] == needs[c_left]: # ???
                        match -= 1
                    window[c_left] -= 1

                left += 1
            right += 1
        return False


if __name__ == '__main__':
    sol = Solution()
    res = sol.checkInclusion2(s1= "ab" , s2 = "eidboaoo")
    print(res)
