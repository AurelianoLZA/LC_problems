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
给你一个二叉树的根节点 root ，按 任意顺序 ，返回所有从根节点到叶子节点的路径。

叶子节点 是指没有子节点的节点。

输入：root = [1,2,3,null,5]
输出：["1->2->5","1->3"]

'''


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        def dfs(node, path):
            if node is None:
                return
            path += str(node.val)
            if node.left is None and node.right is None:
                res.append(path)
                return
            path += str("->")
            dfs(node.left, path)
            dfs(node.right,path)

        res = []
        dfs(root, "")
        return res

