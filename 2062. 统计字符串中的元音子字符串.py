import collections
import functools
import math
from typing import List
from typing import Optional

'''
子字符串 是字符串中的一个连续（非空）的字符序列。

元音子字符串 是 仅 由元音（'a'、'e'、'i'、'o' 和 'u'）组成的一个子字符串，且必须包含 全部五种 元音。

给你一个字符串 word ，统计并返回 word 中 元音子字符串的数目 。
输入：word = "cuaieuouac"
输出：7
解释：下面列出 word 中的元音子字符串（斜体加粗部分）：
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
'''


class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vows = set(["a","e","i","o","u"])

        count = 0
        for i in range(len(word)):
            for right in range(i, len(word)):
                if set(list(word[i:right+1])) == vows:
                    count += 1

        return count

if __name__ == '__main__':
    sol = Solution()
    res = sol.countVowelSubstrings("aeiouu")
    res = sol.countVowelSubstrings("cuaieuouac")
    print(res)
