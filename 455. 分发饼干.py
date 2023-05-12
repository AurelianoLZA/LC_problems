import collections
import functools
import math
from typing import List
from typing import Optional

'''
假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。

对每个孩子 i，都有一个胃口值 g[i]，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j，都有一个尺寸 s[j] 。
如果 s[j] >= g[i]，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。你的目标是尽可能满足越多数量的孩子，
并输出这个最大数值。  
'''


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        kids = sorted(g)
        cookies = sorted(s)
        kids_index = 0
        for cookie in cookies:
            if kids_index < len(kids) and cookie >= kids[kids_index]:
                count += 1
                kids_index += 1
            else:
                continue
        return count




if __name__ == '__main__':
    sol = Solution()
    res = sol.findContentChildren(g = [1,2,3], s = [1,1])
    print(res)
