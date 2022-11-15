import collections
import functools
import math
from typing import List
from typing import Optional

'''

'''


class StockSpanner:
    ls = []

    def __init__(self):
        self.ls = []

    def next(self, price: int) -> int:
        self.ls.append(price)

        count = 0
        k = len(self.ls)-1
        while (k >= 0 and self.ls[k] <= price):
            k -= 1
            count += 1
        return count


obj = StockSpanner()
print(obj.next(100))
print(obj.next(80))
print(obj.next(60))
print(obj.next(70))

