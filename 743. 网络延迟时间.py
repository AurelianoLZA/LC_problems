import collections
import functools
import math
from typing import List
from typing import Optional

'''
有 n 个网络节点，标记为 1 到 n。

给你一个列表 times，表示信号经过 有向 边的传递时间。 times[i] = (ui, vi, wi)，其中 ui 是源节点，vi 是目标节点， wi 是一个信号从源节点传递到目标节点的时间。

现在，从某个节点 K 发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1 。

输入：times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
输出：2
'''


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        connections = collections.defaultdict(list)
        weights = collections.defaultdict(int)
        for time in times:
            connections[time[0]].append(time[1])
            weights[(time[0], time[1])] = time[2]
        visited = [False] * n

        def dfs(node, weight):
            nonlocal res
            if visited[node-1]:
                return
            visited[node-1] = True
            if all(visited):
                res = weight
                return
            if not connections[node]:
                return
            for next in connections[node]:
                dfs(next, weight + weights[(node, next)])
        res = -1
        dfs(k, 0)
        return res





sol = Solution()
res = sol.networkDelayTime(times = [[1,2,1],[2,1,3]], n = 2, k = 2)
print(res)
