import collections
import functools
import math
from typing import List
from typing import Optional

'''
给定三个字符串 s1、s2、s3，请你帮忙验证 s3 是否是由 s1 和 s2 交错 组成的。

两个字符串 s 和 t 交错 的定义与过程如下，其中每个字符串都会被分割成若干 非空 子字符串：
'''


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        redindex, blueindex = 0, 0
        for index in range(len(s3)):
            if redindex < len(s1) and s3[index] == s1[redindex]:
                redindex += 1
            elif blueindex < len(s2) and s3[index] == s2[blueindex]:
                blueindex += 1
            elif redindex < len(s1) and blueindex < len(s2):
                return False
        return redindex == len(s1)-1 and blueindex == len(s2)-1


if __name__ == '__main__':
    sol = Solution()
    res = sol.isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac")
    print(res)
