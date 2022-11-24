import collections
import functools
import math
from typing import List
from typing import Optional

'''
某种外星语也使用英文小写字母，但可能顺序 order 不同。字母表的顺序（order）是一些小写字母的排列。

给定一组用外星语书写的单词 words，以及其字母表的顺序 order，只有当给定的单词在这种外星语中按字典序排列时，返回 true；否则，返回 false。

输入：words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
输出：true
解释：在该语言的字母表中，'h' 位于 'l' 之前，所以单词序列是按字典序排列的。

'''


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(set(words)) == 1:
            return True

        temp = pairwise([order.index(c) for c in word] for word in words)

        return all(s <= t for s, t in temp)



sol = Solution()
res = sol.isAlienSorted(words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz")
print(res)
