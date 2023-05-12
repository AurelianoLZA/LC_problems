import collections
import functools
import math
from typing import List
from typing import Optional

'''
在歌曲列表中，第 i 首歌曲的持续时间为 time[i] 秒。

返回其总持续时间（以秒为单位）可被 60 整除的歌曲对的数量。
形式上，我们希望下标数字 i 和 j 满足  i < j 且有 (time[i] + time[j]) % 60 == 0。
'''


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        cnt = 0
        for i in range(len(time)):
            for j in range(i+1, len(time)):
                if (time[i] + time[j]) % 60 == 0:
                    cnt += 1
        return cnt


if __name__ == '__main__':
    sol = Solution()
    res = sol.numPairsDivisibleBy60(time = [30,20,150,100,40]
)
    print(res)
