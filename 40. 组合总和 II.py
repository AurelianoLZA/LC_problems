import collections
import functools
import math
from typing import List
from typing import Optional

'''
给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用 一次 。
'''


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(candidates, index, ls, cursum, target, res):
            if cursum > target:
                return
            if cursum == target:
                res.append(ls)
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                dfs(candidates, i+1, ls + [candidates[i]], cursum + candidates[i], target, res)

        res = []
        candidates.sort()
        dfs(candidates, 0, [], 0, target, res)
        return res


if __name__ == '__main__':
    sol = Solution()
    res = sol.combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8,)
    print(res)
