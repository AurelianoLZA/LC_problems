import collections
import functools
import math
from typing import List
from typing import Optional

'''
在无限的平面上，机器人最初位于 (0, 0) 处，面朝北方。注意:

北方向 是y轴的正方向。
南方向 是y轴的负方向。
东方向 是x轴的正方向。
西方向 是x轴的负方向。
机器人可以接受下列三条指令之一：

"G"：直走 1 个单位
"L"：左转 90 度
"R"：右转 90 度
机器人按顺序执行指令 instructions，并一直重复它们。

只有在平面中存在环使得机器人永远无法离开时，返回 true。否则，返回 false。
'''


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        index = 0
        pos = [0,0]
        ls = [instructions for _ in range(100)]
        for instructions in ls:
            for instruction in instructions:

                if instruction == "G":
                    pos[0] += directions[index][0]
                    pos[1] += directions[index][1]
                elif instruction == "L":
                    index = (index-1)%4
                else:
                    index = (index+1)%4
            if pos == [0,0]:
                return True

        return False


sol = Solution()
res = sol.isRobotBounded("GLGLGGLGL")
print(res)
