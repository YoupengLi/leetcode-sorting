# -*- coding: utf-8 -*-
# @Time    : 2019/7/11 10:39
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0130_solve.py
# @Software: PyCharm

'''
130. Surrounded Regions

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:
X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:
X X X X
X X X X
X X X X
X O X X

Explanation:
Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board
are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border
will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

题目解析：只要把除边界上所有的'O'以及与之相连的'O'外，所有'O'变换成'X'即可。
解题思路：BFS
1.找到边界上连通的'O',将其进行保存；
2.把其他所有的'O'进行变换。
'''

from collections import deque

class Solution:
    def solve(self, board: 'List[List[str]]') -> 'None':
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        queue = deque()
        for r in range(len(board)):
            for c in range(len(board[0])):
                if (r in [0, len(board) - 1] or c in [0, len(board[0]) - 1]) and board[r][c] == "O":
                    queue.append((r, c))
        while queue:
            r, c = queue.popleft()
            if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == "O":
                board[r][c] = "D"
                queue.append((r - 1, c))
                queue.append((r + 1, c))
                queue.append((r, c - 1))
                queue.append((r, c + 1))

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "D":
                    board[r][c] = "O"

    def solve_1(self, board: 'List[List[str]]') -> 'None':
        """
        Do not return anything, modify board in-place instead.
        """
        # 1. Replace all 'O' with 'D'
        # 2. Call 'D' on the edges and replace them with 'O'
        # 3. Replace rest of the 'D' with 'X'
        # check base cases
        if not board or not board[0]:
            return

        if len(board) <= 2 or len(board[0]) <= 2:
            return

        # check top and bottom edges
        for j in range(len(board[0])):
            if board[0][j] == 'O':
                self.dfs(0, j, board, 'O', 'D')
            if board[len(board) - 1][j] == 'O':
                self.dfs(len(board) - 1, j, board, 'O', 'D')

        # check left and right edges
        for i in range(len(board)):
            if board[i][0] == 'O':
                self.dfs(i, 0, board, 'O', 'D')
            if board[i][len(board[i]) - 1] == 'O':
                self.dfs(i, len(board[i]) - 1, board, 'O', 'D')

        # replace all the 'O' with 'X', and 'D' with 'O'
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'D':
                    board[i][j] = 'O'

    def dfs(self, i: 'int', j: 'int', board: 'List[List[str]]', checkLetter: 'str', changeTo: 'str'):
        if not (0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == checkLetter) :
            return

        board[i][j] = changeTo

        # check top
        self.dfs(i + 1, j, board, checkLetter, changeTo)
        # check bottom
        self.dfs(i - 1, j, board, checkLetter, changeTo)
        # check left
        self.dfs(i, j - 1, board, checkLetter, changeTo)
        # check right
        self.dfs(i, j + 1, board, checkLetter, changeTo)

if __name__ == "__main__":
    a = Solution()
    board = [['X', 'X', 'X', 'X'],
             ['X', 'O', 'O', 'X'],
             ['X', 'X', 'O', 'X'],
             ['X', 'O', 'X', 'X']]
    a.solve(board)
    print(board)
    board = [['X', 'X', 'X', 'X'],
             ['X', 'O', 'O', 'X'],
             ['X', 'X', 'O', 'X'],
             ['X', 'O', 'X', 'X']]
    a.solve_1(board)
    print(board)