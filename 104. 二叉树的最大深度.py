import collections
import functools
import math
from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，
'''


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node, depth):
            nonlocal res
            if node is None:
                res = max(res, depth)
                return
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        dfs(root, 0)
        return res

