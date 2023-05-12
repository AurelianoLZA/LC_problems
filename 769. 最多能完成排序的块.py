import collections
import functools
import math
from typing import List
from typing import Optional

'''
给定一个长度为 n 的整数数组 arr ，它表示在 [0, n - 1] 范围内的整数的排列。

我们将 arr 分割成若干 块 (即分区)，并对每个块单独排序。将它们连接起来后，使得连接的结果和按升序排序后的原数组相同。

返回数组能分成的最多块数量。
'''


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        counter = 1
        currmax = arr[0]
        currmin = -1
        for i in range(len(arr)):
            val = arr[i]
            if val > currmax:
                counter += 1
                currmax = val
            elif val < currmin:
                counter += 1
                currmin = val
        return counter


if __name__ == '__main__':
    sol = Solution()
    res = sol.maxChunksToSorted(arr = [1,0,2,3,4])
    print(res)
