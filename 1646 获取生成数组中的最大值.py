import collections
import functools
import math
from typing import List
from typing import Optional

'''

'''


class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return  0
        ls = [0] * (n+1)
        ls[0], ls[1] = 0,1
        for i in range(2, len(ls)):
            if i % 2 == 0:
                ls[i] = ls[i//2]
            else:
                ls[i] = ls[i//2] + ls[i//2 + 1]
        return max(ls)



sol = Solution()
res = sol.getMaximumGenerated(7)
print(res)
