import collections
import functools
import math
from typing import List
from typing import Optional
import re

'''
给定一个段落 (paragraph) 和一个禁用单词列表 (banned)。返回出现次数最多，同时不在禁用列表中的单词。

题目保证至少有一个词不在禁用列表中，而且答案唯一。

禁用列表中的单词用小写字母表示，不含标点符号。段落中的单词不区分大小写。答案都是小写字母。

输入: 
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
输出: "ball"
解释: 
"hit" 出现了3次，但它是一个禁用的单词。
"ball" 出现了2次 (同时没有其他单词出现2次)，所以它是段落里出现次数最多的，且不在禁用列表中的单词。 

'''


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        ls = re.split("\.|\,| ", paragraph) # 用正则按照多种（，。空格） 分割字符串
        ls = list(map(lambda x : x.lower(), ls))
        ls = list(filter(lambda x : x != "", ls))
        print(ls)
        for i in range(len(ls)):
            if not str(ls[i][-1]).isalpha():
                ls[i] = ls[i][:-1]
        for ban in banned:
            while ban in ls:
                ls.remove(ban)

        d = collections.Counter(ls)
        res = sorted(d.items(), key = lambda x : -x[1]) # 根据frequency 降序排列（最多次数的在index 0 ）
        return res[0][0]


sol = Solution()
res = sol.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])
print(res)
