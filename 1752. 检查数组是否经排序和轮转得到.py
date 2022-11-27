import collections
import functools
import math
from typing import List
from typing import Optional

'''
给你一个数组 nums 。nums 的源数组中，所有元素与 nums 相同，但按非递减顺序排列。

如果 nums 能够由源数组轮转若干位置（包括 0 个位置）得到，则返回 true ；否则，返回 false 。

源数组中可能存在 重复项 。

输入：nums = [3,4,5,1,2]
输出：true
解释：[1,2,3,4,5] 为有序的源数组。
可以轮转 x = 3 个位置，使新数组从值为 3 的元素开始：[3,4,5,1,2] 。
'''


class Solution:
    def check(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            nums.append(nums.pop(0))
            if sorted(nums) == nums:
                return True
        return False



if __name__ == '__main__':
    sol = Solution()
    res = sol.check(nums = [3,4,5,1,2])
    res = sol.check([2,1,3,4])
    print(res)
