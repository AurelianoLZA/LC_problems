import collections
import functools
import math
from typing import List
from typing import Optional

'''
假设 Andy 和 Doris 想在晚餐时选择一家餐厅，并且他们都有一个表示最喜爱餐厅的列表，每个餐厅的名字用字符串表示。

你需要帮助他们用最少的索引和找出他们共同喜爱的餐厅。 如果答案不止一个，则输出所有答案并且不考虑顺序。 你可以假设答案总是存在。
'''


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common = {}
        for index1 in range(len(list1)):
            if list1[index1] in list2:
                common[list1[index1]] = index1 + list2.index(list1[index1])
        res = []
        minindex = min(common.values())
        for rest, indexsum in common.items():
            if indexsum == minindex:
                res.append(rest)
        return res



if __name__ == '__main__':
    sol = Solution()
    res = sol.findRestaurant(list1 = ["Shogun","Tapioca Express","Burger King","KFC"],
                             list2 = ["KFC","Shogun","Burger King", "Shogun"])
    print(res)
