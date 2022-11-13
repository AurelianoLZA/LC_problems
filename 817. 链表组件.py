import collections
import functools
import math
from typing import List
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
给定链表头结点 head，该链表上的每个结点都有一个 唯一的整型值 。同时给定列表 nums，该列表是上述链表中整型值的一个子集。

返回列表 nums 中组件的个数，这里对组件的定义为：链表中一段最长连续结点的值（该值必须在列表 nums 中）构成的集合。

输入: head = [0,1,2,3], nums = [0,1,3]
输出: 2
解释: 链表中,0 和 1 是相连接的，且 nums 中不包含 2，所以 [0, 1] 是 nums 的一个组件，同理 [3] 也是一个组件，故返回 2。

https://leetcode.cn/problems/linked-list-components/description/

'''


class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        curr = head
        res = 0
        while (curr is not None):
            if curr.val in nums:
                while curr and curr.val in nums:
                    curr = curr.next
                res += 1
            else:
                curr = curr.next
        return res


