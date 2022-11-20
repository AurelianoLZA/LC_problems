import collections
import functools
import math
from typing import List
from typing import Optional

'''
给你一个字符串 s。请你按照单词在 s 中的出现顺序将它们全部竖直返回。
单词应该以字符串列表的形式返回，必要时用空格补位，但输出尾部的空格需要删除（不允许尾随空格）。
每个单词只能放在一列上，每一列中也只能有一个单词。

输入：s = "TO BE OR NOT TO BE"
输出：["TBONTB","OEROOE","   T"]
解释：题目允许使用空格补位，但不允许输出末尾出现空格。
"TBONTB"
"OEROOE"
"   T"
'''


class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split(" ")
        ls = [[] for _ in range(max([len(word) for word in words]))]
        for word in words:
            for index in range(len(word)):
                ls[index].append(word[index])
            for i in range(len(word), len(ls)):
                ls[i].append(" ")
        print(ls)
        res = ["".join(arr).rstrip() for arr in ls]
        return res


sol = Solution()
res = sol.printVertically("TO BE OR NOT TO BE")
print(res)
