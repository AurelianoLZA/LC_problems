import collections
import functools
import math
from typing import List
from typing import Optional

'''
给你一个字符串 licensePlate 和一个字符串数组 words ，请你找出 words 中的 最短补全词 。

补全词 是一个包含 licensePlate 中所有字母的单词。忽略 licensePlate 中的 数字和空格 。不区分大小写。如果某个字母在 licensePlate 中出现不止一次，那么该字母在补全词中的出现次数应当一致或者更多。

例如：licensePlate = "aBc 12c"，那么它的补全词应当包含字母 'a'、'b' （忽略大写）和两个 'c' 。可能的 补全词 有 "abccdef"、"caaacab" 以及 "cbca" 。

请返回 words 中的 最短补全词 。题目数据保证一定存在一个最短补全词。当有多个单词都符合最短补全词的匹配条件时取 words 中 第一个 出现的那个。

输入：licensePlate = "1s3 PSt", words = ["step", "steps", "stripe", "stepple"]
输出："steps"
解释：最短补全词应该包括 "s"、"p"、"s"（忽略大小写） 以及 "t"。
"step" 包含 "t"、"p"，但只包含一个 "s"，所以它不符合条件。
"steps" 包含 "t"、"p" 和两个 "s"。
"stripe" 缺一个 "s"。
"stepple" 缺一个 "s"。
因此，"steps" 是唯一一个包含所有字母的单词，也是本例的答案。
'''


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        def helper(word):
            col = collections.Counter(word)
            for key, value in lookup.items():
                if key not in col.keys() or col[key] != value:
                    return False
            return True
        lookup = collections.defaultdict(int)
        for ch in licensePlate:
            if not ch.isalpha():
                continue
            lookup[ch.lower()] += 1
        words.sort(key=lambda word: len(word))
        for word in words:
            if helper(word):
                return word
        return ""

    def shortestCompletingWord2(self, licensePlate: str, words: List[str]) -> str:

        res = " " * (max([len(word) for word in words])+1)
        counter = collections.Counter(list(map(lambda z: z.lower(), list(filter(lambda x : x.isalpha(), list(licensePlate))))))
        for word in words:
            flag = True
            counter_word = collections.Counter(word)
            for key, value in counter.items():
                if key not in counter_word.keys() or value > counter_word[key]:
                    flag &= False
            if flag and len(word) < len(res):
                res = word
        return res


sol = Solution()
res = sol.shortestCompletingWord2(licensePlate = "1s3 PSt", words = ["step", "steps", "stripe", "stepple"])
print(res)
