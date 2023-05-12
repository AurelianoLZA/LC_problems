import collections
import functools
import math
from typing import List
from typing import Optional

'''
给你一个二叉树的根节点 root ， 检查它是否轴对称。
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        root1, root2 = root, root
        def dfs(node1, node2):
            if node1 is None and node2 is None:
                return True
            if node1 is None or node2 is None:
                return False
            return node1.val == node2.val and dfs(node1.left, node2.right) and dfs(node1.right, node2.left)
        return dfs(root1, root2)

