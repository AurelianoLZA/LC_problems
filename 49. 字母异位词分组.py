import collections
import functools
import math
from typing import List
from typing import Optional

'''
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。

字母异位词 是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母通常恰好只用一次。

输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]

思路 ： 所有字母异位词sort之后都是一样的，所以可以根据sorted（str）的结果当作字典的key，值为所有的字母异位词

'''


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        d = collections.defaultdict(list)
        for str in strs:
            d["".join(sorted(str))].append(str)
        for value in d.values():
            res.append(value)
        return res

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        dict = collections.defaultdict(list)
        for str in strs:
            dict["".join(sorted(str))].append(str)
        res = []
        for value in dict.values():
            res.append(value)
        return res



sol = Solution()
res = sol.groupAnagrams2(["eat", "tea", "tan", "ate", "nat", "bat"])
print(res)
