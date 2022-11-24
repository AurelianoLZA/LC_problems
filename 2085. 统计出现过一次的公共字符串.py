import collections
import functools
import math
from typing import List
from typing import Optional

'''
给你两个字符串数组 words1 和 words2 ，请你返回在两个字符串数组中 都恰好出现一次 的字符串的数目。

输入：words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"]
输出：2
解释：
- "leetcode" 在两个数组中都恰好出现一次，计入答案。
- "amazing" 在两个数组中都恰好出现一次，计入答案。
- "is" 在两个数组中都出现过，但在 words1 中出现了 2 次，不计入答案。
- "as" 在 words1 中出现了一次，但是在 words2 中没有出现过，不计入答案。
所以，有 2 个字符串在两个数组中都恰好出现了一次。
'''


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        c1 = collections.Counter(words1)
        c2 = collections.Counter(words2)
        res = 0
        for key, val in c1.items():
            if key in c2.keys() and val == c2[key] == 1:
                res += 1
        return res




if __name__ == '__main__':
    sol = Solution()
    res = sol.countWords(words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"])
    print(res)
