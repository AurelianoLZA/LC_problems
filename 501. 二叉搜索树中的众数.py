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
给你一个含重复值的二叉搜索树（BST）的根节点 root ，找出并返回 BST 中的所有 众数（即，出现频率最高的元素）。

如果树中有不止一个众数，可以按 任意顺序 返回。

假定 BST 满足如下定义：

结点左子树中所含节点的值 小于等于 当前节点的值
结点右子树中所含节点的值 大于等于 当前节点的值
左子树和右子树都是二叉搜索树

'''


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if node is None:
                return
            ls.append(node.val)
            dfs(node.left)
            dfs(node.right)
        ls = []
        dfs(root)
        d = collections.Counter(ls)
        res = []
        maxFreq = max(d.values())
        for key, value in d.items():
            if value == maxFreq:
                res.append(key)
        return res



sol = Solution()
res = sol.findMode(TreeNode(1, None, TreeNode(2, TreeNode(2), None)))
print(res)
