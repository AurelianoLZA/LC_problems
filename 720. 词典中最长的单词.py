import collections
import functools
import math
from typing import List
from typing import Optional

'''
给出一个字符串数组 words 组成的一本英语词典。返回 words 中最长的一个单词，该单词是由 words 词典中其他单词逐步添加一个字母组成。

若其中有多个可行的答案，则返回答案中字典序最小的单词。若无答案，则返回空字符串。

输入：words = ["w","wo","wor","worl", "world"]
输出："world"
解释： 单词"world"可由"w", "wo", "wor", 和 "worl"逐步添加一个字母组成。
'''


class Trie:

    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def searchPrefix(self, prefix: str) -> "Trie":
        node = self
        for w in prefix:
            ch = ord(w) - ord('a')
            if node.children[ch] is None or not node.children[ch].isEnd:
                return None
            node = node.children[ch]
        return node


    def insert(self, word: str) -> None:
        node = self
        for w in word:
            ch = ord(w) - ord('a')
            if node.children[ch] is None:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node is not None and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        return self.searchPrefix(prefix) is not None

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)
        words.sort(key=lambda x : len(x))
        res = ""
        for word in words:
            if trie.search(word) is not None and len(word) > len(res):
                res = word
        return res


if __name__ == '__main__':
    sol = Solution()
    res = sol.longestWord(words = ["w","wo","wor","worl", "world"])
    print(res)
