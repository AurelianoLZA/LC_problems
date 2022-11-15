import collections
import functools
import math
from typing import List
from typing import Optional

'''
给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。

叶子节点 是指没有子节点的节点。

输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：[[5,4,11,2],[5,8,4,5]]
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, ls):
            nonlocal res
            if node is None:
                return
            if node.left is None and node.right is None:
                if sum(ls) + node.val == targetSum:
                    ls.append(node.val)
                    res.append(ls)
            ls.append(node.val)
            dfs(node.left, ls)
            dfs(node.right, ls)
        res = []
        dfs(root, [])
        return res



# sol = Solution()
# res = sol.
# print(res)
