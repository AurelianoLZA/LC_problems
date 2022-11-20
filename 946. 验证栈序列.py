import collections
import functools
import math
from typing import List
from typing import Optional

'''
给定 pushed 和 popped 两个序列，每个序列中的 值都不重复，只有当它们可能是在最初空栈上
进行的推入 push 和弹出 pop 操作序列的结果时，返回 true；否则，返回 false 。

输入：pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
输出：true
解释：我们可以按以下顺序执行：
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
'''


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        index1, index2 = 0 ,0
        ls = []
        for pushItem in pushed:
            ls.append(pushItem)
            while ls and popped[index2] == ls[-1]:
                ls.pop()
                index2 += 1
        print(ls)

        return not ls


sol = Solution()
res = sol.validateStackSequences(pushed = [1,2,3,4,5], popped = [4,5,3,2,1])
res = sol.validateStackSequences(pushed = [1,2,3,4,5], popped = [4,3,5,1,2])
print(res)
