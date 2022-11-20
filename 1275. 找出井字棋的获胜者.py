import collections
import functools
import math
from typing import List
from typing import Optional

'''
A 和 B 在一个 3 x 3 的网格上玩井字棋。

井字棋游戏的规则如下：

玩家轮流将棋子放在空方格 (" ") 上。
第一个玩家 A 总是用 "X" 作为棋子，而第二个玩家 B 总是用 "O" 作为棋子。
"X" 和 "O" 只能放在空方格中，而不能放在已经被占用的方格上。
只要有 3 个相同的（非空）棋子排成一条直线（行、列、对角线）时，游戏结束。
如果所有方块都放满棋子（不为空），游戏也会结束。
游戏结束后，棋子无法再进行任何移动。
给你一个数组 moves，其中每个元素是大小为 2 的另一个数组（元素分别对应网格的行和列），它按照 A 和 B 的行动顺序（先 A 后 B）记录了两人各自的棋子位置。

如果游戏存在获胜者（A 或 B），就返回该游戏的获胜者；如果游戏以平局结束，则返回 "Draw"；如果仍会有行动（游戏未结束），则返回 "Pending"。

你可以假设 moves 都 有效（遵循井字棋规则），网格最初是空的，A 将先行动。
输入：moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
输出："A"
解释："A" 获胜，他总是先走。
"X  "    "X  "    "X  "    "X  "    "X  "
"   " -> "   " -> " X " -> " X " -> " X "
"   "    "O  "    "O  "    "OO "    "OOX"
'''


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        def win(matrix, letter):
            for i in range(3):
                if matrix[i][0] == letter and matrix[i][1] == letter and matrix[i][2] == letter:
                    return True
            for j in range(3):
                if matrix[0][j] == letter and matrix[1][j] == letter and matrix[2][j] == letter:
                    return True
            if matrix[0][0] == matrix[1][1] == matrix[2][2] == letter:
                return True
            if matrix[0][2] == matrix[1][1] == matrix[2][0] == letter:
                return True
            return False



        matrix = [["" for _ in range(3)] for _ in range(3)]
        flag = 1
        for move in moves:
            if flag == 1 :
                matrix[move[0]][move[1]] = "X"
            else :
                matrix[move[0]][move[1]] = "O"
            if win(matrix, "X"):
                return "A"
            if win(matrix, "O"):
                return "B"
            flag = -flag
        return "Draw" if len(moves) == 9 else "Pending"



sol = Solution()
res = sol.tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]])
res = sol.tictactoe([[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]])
res = sol.tictactoe([[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]])
print(res)
