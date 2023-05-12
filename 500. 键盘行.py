import collections
import functools
import math
from typing import List
from typing import Optional

'''
给你一个字符串数组 words ，只返回可以使用在 美式键盘 同一行的字母打印出来的单词。键盘如下图所示。

美式键盘 中：

第一行由字符 "qwertyuiop" 组成。
第二行由字符 "asdfghjkl" 组成。
第三行由字符 "zxcvbnm" 组成。

输入：words = ["Hello","Alaska","Dad","Peace"]
输出：["Alaska","Dad"]
'''


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        lines = [ "qwertyuiop" , "asdfghjkl", "zxcvbnm"]
        def helper(word):
            l = ""
            for line in lines:
                if word[0].lower() in line:
                    l = line
            return False not in [c.lower() in l for c in word]
        ls = list(filter(helper, words))
        return ls

    def findWords2(self, words: List[str]) -> List[str]:
        lines = [ "qwertyuiop" , "asdfghjkl", "zxcvbnm"]
        res=  []
        def helper(word):
            l = ""
            for line in lines:
                if word[0].lower() in line:
                    l = line
            return False not in [ch.lower() in l for ch in word]
        return list(filter(helper, words))




sol = Solution()
res = sol.findWords2(["Hello","Alaska","Dad","Peace"])
print(res)
