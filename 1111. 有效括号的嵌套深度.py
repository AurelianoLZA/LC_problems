import collections
import functools
import math
from typing import List
from typing import Optional

'''
有效括号字符串 定义：对于每个左括号，都能找到与之对应的右括号，反之亦然。详情参见题末「有效括号字符串」部分。

嵌套深度 depth 定义：即有效括号字符串嵌套的层数，depth(A) 表示有效括号字符串 A 的嵌套深度。详情参见题末「嵌套深度」部分。

有效括号字符串类型与对应的嵌套深度计算方法如下图所示：
划分方案用一个长度为 seq.length 的答案数组 answer 表示，编码规则如下：

answer[i] = 0，seq[i] 分给 A 。
answer[i] = 1，seq[i] 分给 B 。

输入：seq = "(()())"
输出：[0,1,1,1,1,0]

思路： 用depthA 和 depthB 分别记录A和B 的深度。如果ch是（， 则加到深度更小的depth；如果ch是）， 则加到深度更大的depth

'''


class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        depthA, depthB = 0, 0
        res = [0] * len(seq)
        for i in range(len(seq)):
            if seq[i] == "(":
                if depthA <= depthB:
                    depthA += 1
                    res[i] = 0
                else:
                    depthB += 1
                    res[i] = 1
            else:
                if depthA >= depthB:
                    depthA -= 1
                    res[i] = 0
                else:
                    depthB -= 1
                    res[i] = 1
        return res


sol = Solution()
res = sol.maxDepthAfterSplit("(()())")
print(res)
