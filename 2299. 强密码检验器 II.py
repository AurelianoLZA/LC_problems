import collections
import functools
import math
from typing import List
from typing import Optional

'''
如果一个密码满足以下所有条件，我们称它是一个 强 密码：

它有至少 8 个字符。
至少包含 一个小写英文 字母。
至少包含 一个大写英文 字母。
至少包含 一个数字 。
至少包含 一个特殊字符 。特殊字符为："!@#$%^&*()-+" 中的一个。
它 不 包含 2 个连续相同的字符（比方说 "aab" 不符合该条件，但是 "aba" 符合该条件）。
给你一个字符串 password ，如果它是一个 强 密码，返回 true，否则返回 false 。

示例 1：

输入：password = "IloveLe3tcode!"
输出：true
解释：密码满足所有的要求，所以我们返回 true 。

'''


class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        ls = list(password)
        repo = list("!@#$%^&*()-+")
        if len(ls) < 8:
            return False
        if not list(filter(lambda x : x.islower(), ls)):
            return False
        if not list(filter(lambda x : x.isupper(), ls)):
            return False
        if not list(filter(lambda x : x.isdigit(), ls)):
            return False
        if not list(filter(lambda x : x in repo, ls)):
            return False
        for i in range(len(ls)-1):
            if ls[i] == ls[i+1]:
                return False
        return True






if __name__ == '__main__':
    sol = Solution()
    res = sol.strongPasswordCheckerII("IloveLe3tcode!")
    res = sol.strongPasswordCheckerII("Me+You--IsMyDream")
    print(res)
