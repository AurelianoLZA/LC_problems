import collections
import functools
import math
from typing import List
from typing import Optional

'''
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明：叶子节点是指没有子节点的节点
'''

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if root is None:
                return 0
            if node.left is None and node.right is None:
                return 1
            m1 = dfs(node.left)
            m2 = dfs(node.right)
            if node.left is None or node.right is None:
                return



sol = Solution()
res = sol.
print(res)
