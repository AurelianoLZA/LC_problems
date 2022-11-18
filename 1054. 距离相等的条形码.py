import collections
import functools
import math
from typing import List
from typing import Optional

'''
在一个仓库里，有一排条形码，其中第 i 个条形码为 barcodes[i]。

请你重新排列这些条形码，使其中任意两个相邻的条形码不能相等。 你可以返回任何满足该要求的答案，此题保证存在答案。

输入：barcodes = [1,1,1,2,2,2]
输出：[2,1,2,1,2,1]
'''


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        res = []
        lookup = collections.Counter(barcodes)
        barcodes.sort(key=lambda x : lookup[x], reverse=True)
        while barcodes:
            if not res:
                res.append(barcodes[0])
                barcodes.pop(0)
                continue
            ls =  list(filter(lambda x :  x != res[-1], barcodes))
            d = collections.Counter(ls)
            ls.sort(key=lambda x : d[x], reverse=True)
            val = ls[0]
            barcodes.remove(val)
            res.append(val)
        return res




sol = Solution()
res = sol.rearrangeBarcodes([7,7,7,8,5,7,5,5,5,8])
print(res)
