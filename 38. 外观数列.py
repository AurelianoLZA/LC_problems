import collections
import functools
import math
from typing import List
from typing import Optional

'''
给定一个正整数 n ，输出外观数列的第 n 项。

「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。

你可以将其视作是由递归公式定义的数字字符串序列：

countAndSay(1) = "1"
countAndSay(n) 是对 countAndSay(n-1) 的描述，然后转换成另一个数字字符串。

'''


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        def helper(str):
            ret = ""
            left, right = 0, 0
            while right < len(str):
                while(right < len(str) and str[left] == str[right]):
                    right += 1
                ret += "{}".format(right-left)
                ret += str[left]
                left = right
            return ret
        s1 = "1"
        for i in range(1, n):
            s1 = helper(s1)
        return s1




if __name__ == '__main__':
    sol = Solution()
    res = sol.countAndSay(5)
    print(res)
