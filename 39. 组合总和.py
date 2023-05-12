import collections
import functools
import math
from typing import List
from typing import Optional

'''
给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。

candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。 
'''


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(candidates, index, ls:List[int], cursum, target, res):
            if cursum > target:
                return
            if cursum == target:
                res.append(ls)
                return
            else:
                for i in range(index, len(candidates)):
                    dfs(candidates, i, ls + [candidates[i]], cursum+candidates[i], target, res)
        res = []
        dfs(candidates, 0, [], 0, target, res)
        return res



if __name__ == '__main__':
    sol = Solution()
    res = sol.combinationSum(candidates = [2,3,6,7], target = 7)
    print(res)
