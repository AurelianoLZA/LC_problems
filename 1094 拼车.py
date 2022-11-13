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


''' 
车上最初有 capacity 个空座位。车 只能 向一个方向行驶（也就是说，不允许掉头或改变方向）

给定整数 capacity 和一个数组 trips ,  trip[i] = [numPassengersi, fromi, toi] 表示第 i 次旅行有 numPassengersi 乘客，
接他们和放他们的位置分别是 fromi 和 toi 。这些位置是从汽车的初始位置向东的公里数。

当且仅当你可以在所有给定的行程中接送所有乘客时，返回 true，否则请返回 false。
输入：trips = [[2,1,5],[3,3,7]], capacity = 4
输出：false

输入：trips = [[2,1,5],[3,3,7]], capacity = 5
输出：true
'''

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        start = min(trips[i][1] for i in range(len(trips)))
        end = max(trips[i][2] for i in range(len(trips)))
        ls = [0] * (end-start+1)
        for trip in trips:
            size = trip[0]
            for j in range(trip[1], trip[2]):
                ls[j-start] += size
        print(ls)
        return False not in [val <= capacity for val in ls]

sol = Solution()
res = sol.carPooling([[2,1,5],[3,3,7]], 5)
print(res)
