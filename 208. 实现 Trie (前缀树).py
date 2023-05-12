import collections
import functools
import math
from typing import List
from typing import Optional

'''

'''


class Trie:

        def __init__(self):
            self.children = [None] * 26
            self.isEnd = False

        def searchPrefix(self, prefix: str) -> "Trie":
            node = self
            for w in prefix:
                ch = ord(w) - ord('a')
                if node.children[ch] is None:
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

    # Your Trie object will be instantiated and called as such:
    # obj = Trie()
    # obj.insert(word)
    # param_2 = obj.search(word)
    # param_3 = obj.startsWith(prefix)

