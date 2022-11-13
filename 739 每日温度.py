import collections
import functools
import math
from typing import List
from typing import Optional

'''

'''


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        超时 ： 35/48
        '''

        res= [0] * len(temperatures)
        for i in range(len(temperatures)-1):
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    res[i] = j-i
                    break
        return res




sol = Solution()
res = sol.dailyTemperatures([73,74,75,71,69,72,76,73])
print(res)
