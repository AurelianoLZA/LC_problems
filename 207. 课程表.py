import collections
import functools
import math
from typing import List
from typing import Optional

'''
你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。

在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。

例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。
'''


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        def dfs(adj, index, flag):
            if flag[index] == -1:
                return True
            if flag[index] == 1:
                return False
            flag[index] = 1
            for node in adj[index]:
                noloop = dfs(adj, node, flag)
                if not noloop:
                    return False
            flag[index] = -1
            return True

        adj = [[] for _ in range(numCourses)]
        for prerequisite in prerequisites:
            frm, to = prerequisite[0], prerequisite[1]
            adj[frm].append(to)
        flag = [0 for _ in range(numCourses)]
        for  i in range(numCourses):
            if not dfs(adj, i, flag):
                return False
        return True

