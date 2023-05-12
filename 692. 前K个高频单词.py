import collections
import functools
import math
from typing import List
from typing import Optional

'''
给定一个单词列表 words 和一个整数 k ，返回前 k 个出现次数最多的单词。

返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率， 按字典顺序 排序。

输入: words = ["i", "love", "leetcode", "i", "love", "coding"], k = 2
输出: ["i", "love"]
解析: "i" 和 "love" 为出现次数最多的两个单词，均为2次。
    注意，按字母顺序 "i" 在 "love" 之前。
'''


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        lookup = collections.Counter(words)
        ls = sorted(list(set(words)), key=lambda x : (-lookup.get(x), x))
        print(ls)
        return ls[:k] if len(ls) > k else ls


if __name__ == '__main__':
    sol = Solution()
    res = sol.topKFrequent(words = ["i", "love", "leetcode", "i", "love", "coding"], k = 2)
    print(res)
