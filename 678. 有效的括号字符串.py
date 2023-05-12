import collections
import functools
import math
from typing import List
from typing import Optional

'''
给定一个只包含三种字符的字符串：（ ，） 和 *，写一个函数来检验这个字符串是否为有效字符串。有效字符串具有如下规则：

任何左括号 ( 必须有相应的右括号 )。
任何右括号 ) 必须有相应的左括号 ( 。
左括号 ( 必须在对应的右括号之前 )。
* 可以被视为单个右括号 ) ，或单个左括号 ( ，或一个空字符串。
一个空字符串也被视为有效字符串。
'''


class Solution:
    def checkValidString(self, s: str) -> bool:
        counterstar = 0
        leftcounter = 0
        for ch in s:
            if ch == '(':
                leftcounter += 1
            elif ch == ')':
                if leftcounter > 0 :
                    leftcounter -= 1
                    continue
                elif counterstar > 0 :
                    counterstar -= 1
                    continue
                else:
                    return False
            elif ch == '*':
                counterstar += 1
        return True if leftcounter == 0 or leftcounter == counterstar else False



if __name__ == '__main__':
    sol = Solution()
    res = sol.checkValidString("")
    print(res)
