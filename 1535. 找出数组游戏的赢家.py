import collections
import functools
import math
from typing import List
from typing import Optional

'''
给你一个由 不同 整数组成的整数数组 arr 和一个整数 k 。

每回合游戏都在数组的前两个元素（即 arr[0] 和 arr[1] ）之间进行。比较 arr[0] 与 arr[1] 的大小，较大的整数将会取得这一回合的胜利并保留在位置 0 ，较小的整数移至数组的末尾。当一个整数赢得 k 个连续回合时，游戏结束，该整数就是比赛的 赢家 。

返回赢得比赛的整数。

题目数据 保证 游戏存在赢家。
'''


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        # lookup = collections.defaultdict(int)
        # for val in arr:
        #     lookup[val] = 0
        # for _ in range(len(arr)):
        #     first = arr.pop(0)
        #     snd = arr.pop(0)
        #     lookup[max(first, snd)] += 1
        #     arr.insert(0, max(first, snd))
        #     arr.append(min(first, snd))
        #     if lookup[max(first, snd)] == k:
        #         return max(first, snd)
        # return max(arr)
        consecutive = 1
        if len(arr) == 2 :
            return max(arr[0], arr[1])
        prev = max(arr[0], arr[1])
        for i in range(2, len(arr)):
            if prev > arr[i]:
                consecutive += 1
                if consecutive == k:
                    return prev
            else:
                consecutive = 1
                prev = arr[i]
        return max(arr)



sol = Solution()
res = sol.getWinner(arr = [1,11,22,33,44,55,66,77,88,99], k = 1000000000)
print(res)
