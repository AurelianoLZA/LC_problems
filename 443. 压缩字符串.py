import collections
import functools
import math
from typing import List
from typing import Optional

'''
给你一个字符数组 chars ，请使用下述算法压缩：

从一个空字符串 s 开始。对于 chars 中的每组 连续重复字符 ：

如果这一组长度为 1 ，则将字符追加到 s 中。
否则，需要向 s 追加字符，后跟这一组的长度。
压缩后得到的字符串 s 不应该直接返回 ，需要转储到字符数组 chars 中。需要注意的是，如果组长度为 10 或 10 以上，则在 chars 数组中会被拆分为多个字符。

请在 修改完输入数组后 ，返回该数组的新长度。

你必须设计并实现一个只使用常量额外空间的算法来解决此问题。
'''


class Solution:
    def compress(self, chars: List[str]) -> int:
        left, right = 0, 0
        res = []
        while right < len(chars):
            while right < len(chars) and chars[right] == chars[left]:
                right += 1
            length = right-left
            if length == 1:
                res.append(chars[left])
            elif length >= 10:
                res.append(chars[left])
                res += [ch for ch in str(length)]
            else:
                res.append(chars[left])
                res.append(str(length))
            left = right
        chars[:] = res[:]
        return len(res)

if __name__ == '__main__':
    sol = Solution()
    res = sol.compress(chars = ["a","a","b","b","c","c","c"])
    # res = sol.compress(chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"])
    print(res)
