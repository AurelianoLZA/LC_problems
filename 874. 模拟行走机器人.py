import collections
import functools
import math
from typing import List
from typing import Optional

'''
机器人在一个无限大小的 XY 网格平面上行走，从点 (0, 0) 处开始出发，面向北方。该机器人可以接收以下三种类型的命令 commands ：

-2 ：向左转 90 度
-1 ：向右转 90 度
1 <= x <= 9 ：向前移动 x 个单位长度
在网格上有一些格子被视为障碍物 obstacles 。第 i 个障碍物位于网格点  obstacles[i] = (xi, yi) 。

机器人无法走到障碍物上，它将会停留在障碍物的前一个网格方块上，但仍然可以继续尝试进行该路线的其余部分。

返回从原点到机器人所有经过的路径点（坐标为整数）的最大欧式距离的平方。（即，如果距离为 5 ，则返回 25 ）

输入：commands = [4,-1,4,-2,4], obstacles = [[2,4]]
输出：65
解释：机器人开始位于 (0, 0)：
1. 向北移动 4 个单位，到达 (0, 4)
2. 右转
3. 向东移动 1 个单位，然后被位于 (2, 4) 的障碍物阻挡，机器人停在 (1, 4)
4. 左转
5. 向北走 4 个单位，到达 (1, 8)
距离原点最远的是 (1, 8) ，距离为 12 + 82 = 65

'''


class Solution:
    '''
    超时 ： 44 / 48
    '''
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [[1,0],[0,-1],[-1,0],[0,1]]
        pos = [0,0]
        index = 3
        maxDist = 0
        for command in commands:
            if command == -1:
                index = (index+1) % 4
            elif command == -2:
                index = (index-1) % 4
            else:
                step = command
                for i in range(step):
                    if [pos[0] + directions[index][0], pos[1] + directions[index][1]] in obstacles:
                        break
                    else:
                        pos[0] += directions[index][0]
                        pos[1] += directions[index][1]
                maxDist = max(maxDist, (pos[0]**2 + pos[1]**2))
        return maxDist






sol = Solution()
res = sol.robotSim([4,-1,4,-2,4], [[2,4]])
print(res)
