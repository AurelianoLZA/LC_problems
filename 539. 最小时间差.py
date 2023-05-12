import collections
import functools
import math
from typing import List
from typing import Optional

'''
给定一个 24 小时制（小时:分钟 "HH:MM"）的时间列表，找出列表中任意两个时间的最小时间差并以分钟数表示。
'''


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def translate_to_minute(time:str):
            hour, minute = time.split(":")[0], time.split(":")[1]
            return int(hour) * 60 + int(minute)

        if len(timePoints) > 60 * 24:
            return 0
        ls = sorted(list(map(translate_to_minute, timePoints)))
        print(ls)
        mindiff = float('inf')
        for i in range(1, len(timePoints)):
            mindiff = min(mindiff, ls[i] - ls[i-1])
        return min(mindiff, 60*24-ls[-1]+ls[0])




if __name__ == '__main__':
    sol = Solution()
    res = sol.findMinDifference(timePoints = ["00:00","23:59","00:00"])
    print(res)
