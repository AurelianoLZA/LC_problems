import collections
import itertools
import math
from typing import List
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 给你一个由 不同 正整数组成的数组 nums ，请你返回满足 a * b = c * d 的元组 (a, b, c, d) 的数量。
# 其中 a、b、c 和 d 都是 nums 中的元素，且 a != b != c != d 。
# 输入：nums = [2,3,4,6]
# 输出：8
# 解释：存在 8 个满足题意的元组：
# (2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
# (3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        # 找到所有的2元组
        ls = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                ls.append([nums[i], nums[j]])

        # 根据二元组的乘积建立字典
        d = collections.defaultdict(int)
        for pair in ls:
            d[pair[0] * pair[1]] += 1

        # count
        res = 0
        for val in d.values():
            if val > 1:
                res += math.factorial(val)//(2 * math.factorial(val-2))
        return res * 8

sol = Solution()
res = sol.tupleSameProduct([2,3,4,6])
print(res)

