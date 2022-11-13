import collections
import functools
import math
from typing import List
from typing import Optional

'''
给你两个字符串 start 和 target ，长度均为 n 。每个字符串 仅 由字符 'L'、'R' 和 '_' 组成，其中：

字符 'L' 和 'R' 表示片段，其中片段 'L' 只有在其左侧直接存在一个 空位 时才能向 左 移动，而片段 'R' 只有在其右侧直接存在一个 空位 时才能向 右 移动。
字符 '_' 表示可以被 任意 'L' 或 'R' 片段占据的空位。
如果在移动字符串 start 中的片段任意次之后可以得到字符串 target ，返回 true ；否则，返回 false 。

输入：start = "_L__R__R_", target = "L______RR"
输出：true
解释：可以从字符串 start 获得 target ，需要进行下面的移动：
- 将第一个片段向左移动一步，字符串现在变为 "L___R__R_" 。
- 将最后一个片段向右移动一步，字符串现在变为 "L___R___R" 。
- 将第二个片段向右移动散步，字符串现在变为 "L______RR" 。
可以从字符串 start 得到 target ，所以返回 true 。

与 777题 完全相同

'''


class Solution:
    def canChange(self, start: str, target: str) -> bool:
        i, j = 0, 0
        n = len(start)
        while(i < n or j < n):
            while(i < n and start[i] == "_"):
                i += 1
            while(j < n and target[j] == "_"):
                j += 1
            if (i == n or j == n):
                return i == j
            if start[i] != target[j]:
                return False
            if start[i] == "L" and j  > i:
                return False
            if start[i] == "R" and j < i:
                return False
            i += 1
            j += 1
        return True


sol = Solution()
res = sol.canChange("_L__R__R_", "L______RR")
res = sol.canChange("R_L_", "__LR")
print(res)
