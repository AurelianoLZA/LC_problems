import collections
import functools
import math
from typing import List
from typing import Optional

'''
给定一个 N 叉树，找到其最大深度。

最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。

输入：root = [1,null,3,2,4,null,5,6]
输出：3

'''


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root == None:
            return 0
        return 1 + max([self.maxDepth(child) for child in root.children], default=0)


