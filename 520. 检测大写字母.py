import collections
import functools
import math
from typing import List
from typing import Optional

'''
我们定义，在以下情况时，单词的大写用法是正确的：

全部字母都是大写，比如 "USA" 。
单词中所有字母都不是大写，比如 "leetcode" 。
如果单词不只含有一个字母，只有首字母大写， 比如 "Google" 。
给你一个字符串 word 。如果大写用法正确，返回 true ；否则，返回 false 。


'''


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if ((word[0].isupper() and False not in [ch.islower() for ch in word[1:]]) or (False not in [ch.islower() for ch in word]) or
 (False not in [ch.isupper() for ch in word])):
            return True
        return False

if __name__ == '__main__':
    sol = Solution()
    res = sol.detectCapitalUse("FlaG")
    print(res)
