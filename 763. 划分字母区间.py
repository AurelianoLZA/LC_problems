import collections
import functools
import math
from typing import List
from typing import Optional

'''
字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。返回一个表示每个字符串片段的长度的列表。

输入：S = "ababcbacadefegdehijhklij"
输出：[9,7,8]
解释：
划分结果为 "ababcbaca", "defegde", "hijhklij"。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。
'''
''' 
思路 ： 首先用字典记录每个letter 出现的最后的位置，然后通过双指针，遍历每个char，同时需要更新char出现的最后位置的index。
如果index == end，说明这一段的所有字符都在start到end的区间了，ls.append(end-start+1) 
'''


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letters = [0] * 26
        for i in range(len(s)):
            ch = s[i]
            letters[ord(ch)-ord("a")] = i
        ls = []
        index = 0
        end = 0
        start = 0
        while index < len(s):
            end  = max(end, letters[ord(s[index])-ord("a")])
            if end == index :
                ls.append(end-start+1)
                start = end + 1
            index += 1
        return ls



sol = Solution()
res = sol.partitionLabels("ababcbacadefegdehijhklij")
print(res)
