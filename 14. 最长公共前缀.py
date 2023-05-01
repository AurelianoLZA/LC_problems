import collections
import functools
import math
from typing import List
from typing import Optional

'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。
输入：strs = ["flower","flow","flight"]
输出："fl"
'''


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        index = 0
        for index in range(min([len(x) for x in strs])):
            ch = strs[0][index]
            if all([strs[i][index] == ch for i in range(1, len(strs))]):
                index += 1
            else:
                break
        return "".join(strs[0][:index])

    def longestCommonPrefix2(self, strs: List[str]) -> str:

        min_len = min([len(x) for x in strs])
        index = 0
        for index in range(min_len):
            ch = strs[0][index]
            if all([strs[i][index] == ch for i in range(len(strs))]):
                index += 1
            else:
                break
        return strs[0][:index]


sol = Solution()
res = sol.longestCommonPrefix2(["flower","flow","flight"])
print(res)
