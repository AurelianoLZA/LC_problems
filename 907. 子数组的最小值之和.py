import collections
import functools
import math
from typing import List
from typing import Optional

'''
给定一个整数数组 arr，找到 min(b) 的总和，其中 b 的范围为 arr 的每个（连续）子数组。

由于答案可能很大，因此 返回答案模 10^9 + 7 。

输入：arr = [3,1,2,4]
输出：17
解释：
子数组为 [3]，[1]，[2]，[4]，[3,1]，[1,2]，[2,4]，[3,1,2]，[1,2,4]，[3,1,2,4]。 
最小值为 3，1，2，4，1，1，2，1，1，1，和为 17。
'''


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        tot = 0
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                subls = arr[i:j+1]
                tot += min(subls)
        return tot


sol = Solution()
res = sol.sumSubarrayMins([3,1,2,4])
print(res)
