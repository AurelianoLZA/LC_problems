import collections
import functools
import math
from typing import List
from typing import Optional

'''
给你二叉树的根节点 root 和一个表示目标和的整数 targetSum 。判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。如果存在，返回 true ；否则，返回 false 。

叶子节点 是指没有子节点的节点。

输入：root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
输出：true
解释：等于目标和的根节点到叶节点路径如上图所示。
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, currsum):
            if node is None:
                return
            if node.left is None and node.right is None:
                if currsum + node.val == targetSum:
                    return True
            return dfs(node.left, currsum + node.val) or dfs(node.right, currsum + node.val)
        res = dfs(root, 0)
        return res if res else False

