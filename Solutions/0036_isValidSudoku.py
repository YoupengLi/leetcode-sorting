# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 0021 08:06
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0036_isValidSudoku.py
# @Software: PyCharm

'''
36. Valid Sudoku

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.
The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:
Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true

Example 2:
Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
The given board contain only digits 1-9 and the character '.'.
The given board size is always 9x9.
'''

class Solution:
    def isValidSudoku(self, board: 'List[List[str]]') -> 'bool':
        dict1 = {}
        dict2 = {0: 1, 1: 1, 2: 1, 3: 2, 4: 2, 5: 2, 6: 3, 7: 3, 8: 3}
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                else:
                    if board[i][j] not in dict1:
                        dict1[board[i][j]] = []
                        dict1[board[i][j]].append([i, j])
                    else:
                        dict1[board[i][j]].append([i, j])
        for i in dict1.keys():
            temp = dict1[i]
            if len(temp) == 1:
                continue
            else:
                for j in range(len(temp)):
                    for k in range(j + 1, len(temp)):
                        if temp[k][0] == temp[j][0] or temp[k][1] == temp[j][1]:
                            return False
                        if dict2[temp[k][0]] == dict2[temp[j][0]] and dict2[temp[k][1]] == dict2[temp[j][1]]:
                            return False
        return True

    def isValidSudoku_1(self, board: 'List[List[str]]') -> 'bool':

        # check row
        for l in board:
            visited = set()
            for i in range(9):
                if l[i] != '.':
                    if l[i] in visited:
                        return False
                    visited.add(l[i])
        # check column
        for i in range(9):
            visited = set()
            for l in board:
                if l[i] != '.':
                    if l[i] in visited:
                        return False
                    visited.add(l[i])

        # check sub-box
        for row in (0, 3, 6):
            for col in (0, 3, 6):
                visited = set()
                for i in range(row, row + 3):
                    for j in range(col, col + 3):
                        if board[i][j] != '.':
                            if board[i][j] in visited:
                                return False
                            visited.add(board[i][j])

        return True

if __name__ == "__main__":
    a = Solution()
    # False
    board = [["8","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]
    res = a.isValidSudoku(board)
    print(res)
    res = a.isValidSudoku_1(board)
    print(res)
    # True
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    res = a.isValidSudoku(board)
    print(res)
    res = a.isValidSudoku_1(board)
    print(res)
    # True
    board =[[".", ".", "5", ".", ".", ".", ".", ".", "6"],
            [".", ".", ".", ".", "1", "4", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", "9", "2", ".", "."],
            ["5", ".", ".", ".", ".", "2", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "3", "."],
            [".", ".", ".", "5", "4", ".", ".", ".", "."],
            ["3", ".", ".", ".", ".", ".", "4", "2", "."],
            [".", ".", ".", "2", "7", ".", "6", ".", "."]]
    res = a.isValidSudoku(board)
    print(res)
    res = a.isValidSudoku_1(board)
    print(res)
    # False
    board = [["8","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]
    res = a.isValidSudoku(board)
    print(res)
    res = a.isValidSudoku_1(board)
    print(res)