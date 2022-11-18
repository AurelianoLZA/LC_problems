import collections
import functools
import math
from typing import List
from typing import Optional

'''

'''


class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        maxVal = max(nums)
        deleted = []
        for i in range(k-1):
            if nums[i] == maxVal:
                return maxVal
            if not nums:
                return -1
            deleted.append(nums.pop(0))
            deleted.sort(reverse=True)
        if nums[0] == maxVal or nums[1] == maxVal:
            return maxVal
        else:
            return deleted[0]





sol = Solution()
res = sol.maximumTop(nums = [5,2,2,4,0,6], k = 4)
print(res)
