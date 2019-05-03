# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 0021 10:09
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0037_solveSudoku.py
# @Software: PyCharm

'''
37. Sudoku Solver

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:
Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.
'''

class Solution:
    def solveSudoku(self, board: 'List[List[str]]') -> 'None':
        """
        Do not return anything, modify board in-place instead.
        """
        def backtrack(board, memo, blanks, pos):
            if pos >= len(blanks):
                return True
            r, c = blanks[pos]
            for i in range(1, 10):
                s = str(i)
                if (r, s) not in memo and (s, c) not in memo and (r // 3, c // 3, s) not in memo:
                    board[r][c] = s
                    # add to set to indicate values have been used
                    memo.add((r, s))
                    memo.add((s, c))
                    memo.add((r // 3, c // 3, s))
                    if backtrack(board, memo, blanks, pos + 1):
                        return True
                    # removing values since current iteration is invalid
                    memo.remove((r, s))
                    memo.remove((s, c))
                    memo.remove((r // 3, c // 3, s))

        if not board:
            return
        N, memo, blanks = len(board), set(), []
        for r in range(N):
            for c in range(N):
                if board[r][c].isdigit():
                    # adding existing values to set
                    memo.add((r, board[r][c]))
                    memo.add((board[r][c], c))
                    memo.add((r // 3, c // 3, board[r][c]))
                # add to list of blanks to backtrack on
                else:
                    blanks.append((r, c))
        backtrack(board, memo, blanks, 0)
        [print(i) for i in board]

    def solveSudoku_1(self, board):
        res = self.dfs(board)
        for n, row in enumerate(res):
            board[n] = ''.join(row)
        [print(i) for i in board]

    def dfs(self, board):
        stack = [board]
        while stack:
            s = stack.pop()
            result = self.fill_board(s)
            if result == 'complete':
                return s
            for r in result:
                stack.append(r)

    def fill_board(self, board):
        digits = set('123456789')
        choice, best = {}, []
        for j in range(9):
            for i in range(9):
                if board[j][i] == '.':
                    square = {board[j // 3 * 3 + y][i // 3 * 3 + x]
                              for y in range(3) for x in range(3)}
                    row = {board[j][x] for x in range(9)}
                    col = {board[y][i] for y in range(9)}
                    rest = digits.difference(square, row, col)
                    if len(rest) == 1:
                        board[j][i] = rest.pop()
                        return self.fill_board(board)
                    elif len(rest) == 0:
                        return ''
                    else:
                        choice[(j, i)] = rest
        if not choice:
            return 'complete'
        y, x = min(choice, key=lambda k: len(choice[k]))
        for n in choice[(y, x)]:
            b = copy.deepcopy(board)
            b[y][x] = n
            best.append(b)
        return best

if __name__ == "__main__":
    a = Solution()
    board = [[".", ".", "5", ".", ".", ".", ".", ".", "6"],
            [".", ".", ".", ".", "1", "4", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", "9", "2", ".", "."],
            ["5", ".", ".", ".", ".", "2", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "3", "."],
            [".", ".", ".", "5", "4", ".", ".", ".", "."],
            ["3", ".", ".", ".", ".", ".", "4", "2", "."],
            [".", ".", ".", "2", "7", ".", "6", ".", "."]]
    res = a.solveSudoku(board)
    res = a.solveSudoku_1(board)

