import collections
import functools
import math
from typing import List
from typing import Optional

'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。
'''


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        right = 0
        while right < len(nums):
            if nums[right] != 0:
                nums[left] = nums[right]
                left += 1
                right += 1
                continue
            else:
                right += 1

        for index in range(left, len(nums)):
            nums[index] = 0
        print(nums)




if __name__ == '__main__':
    sol = Solution()
    res = sol.moveZeroes(nums = [0,1,0,3,12])
    print(res)
