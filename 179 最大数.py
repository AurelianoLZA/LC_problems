import collections
import functools
import math
from typing import List
from typing import Optional

'''
给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。

注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。

输入：nums = [10,2]
输出："210"

1 定义compare函数，判断两个string哪种排列的结果更大）如： 4， 42 =》 442 》 424 
2 把原来的nums 数组map 成 str类型的数组
3 用定义的compare 函数sort。functool.cmp_to_key(compare)可以把compare函数用到key

'''


class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        def compare(x : str,y :str):
            return int(y+x) - int(x+y)
        strs = list(map(str, nums))
        strs.sort(key=functools.cmp_to_key(compare))
        return "".join(strs) if strs[0] != "0" else "0"


        # nums = [str(i) for i in nums]
        # def backtrack(index):
        #     if index == len(nums):
        #         res.append(nums[:])
        #     for i in range(index, len(nums)):
        #         nums[i], nums[index] = nums[index], nums[i]
        #         backtrack(index+1)
        #         nums[i], nums[index] = nums[index], nums[i]
        # res = []
        # backtrack(0)
        # maxVal = 0
        # for comb in res:
        #     maxVal = max(maxVal, int("".join(comb)))
        # return maxVal






sol = Solution()
res = sol.largestNumber([0,9,8,7,6,5,4,3,2,1])
print(res)
