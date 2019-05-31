# -*- coding: utf-8 -*-
# @Time    : 2019/5/31 9:27
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0079_exist.py
# @Software: PyCharm

'''
79. Word Search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

Example:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
'''
import collections

class Solution:
    def exist(self, board: 'List[List[str]]', word: 'str') -> 'bool':
        if not board or not board[0]:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

        # check whether can find word, start at (i,j) position
    def dfs(self, board, i, j, word):
        if len(word) == 0:  # all the characters are checked
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
            return False
        tmp = board[i][j]  # first character is found, check the remaining part
        board[i][j] = "#"  # avoid visit agian
        # check whether can find "word" along one direction
        res = self.dfs(board, i + 1, j, word[1:]) or self.dfs(board, i - 1, j, word[1:]) \
            or self.dfs(board, i, j + 1, word[1:]) or self.dfs(board, i, j - 1, word[1:])
        board[i][j] = tmp
        return res

    def exist_1(self, board: 'List[List[str]]', word: 'str') -> 'bool':
        if not board or not board[0] or not word:
            return False

        bcnts = collections.Counter(c for x in board for c in x)
        for c, cnt in collections.Counter(word).items():
            if c not in bcnts or cnt > bcnts[c]:
                return False

        m, n = len(board), len(board[0])
        def dfs(i, x, y):
            if i >= len(word):
                return True

            c = board[x][y]
            board[x][y] = ''

            if x > 0 and board[x - 1][y] == word[i] and dfs(i + 1, x - 1, y):
                return True
            if x + 1 < m and board[x + 1][y] == word[i] and dfs(i + 1, x + 1, y):
                return True
            if y > 0 and board[x][y - 1] == word[i] and dfs(i + 1, x, y - 1):
                return True
            if y + 1 < n and board[x][y + 1] == word[i] and dfs(i + 1, x, y + 1):
                return True

            board[x][y] = c
            return False

        return any(dfs(1, x, y) for x in range(m) for y in range(n) if board[x][y] == word[0])

if __name__ == "__main__":
    a = Solution()
    board =[['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']]
    word = "ABCCED"
    res = a.exist(board, word)
    print(res)
    word = "SEE"
    res = a.exist_1(board, word)
    print(res)
    word = "ABCB"
    res = a.exist(board, word)
    print(res)