# -*- coding: utf-8 -*-
# @Time    : 2019/8/29 0029 20:58
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0200_numIslands.py
# @Software: PyCharm

'''
200. Number of Islands

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input:
11110
11010
11000
00000
Output: 1

Example 2:
Input:
11000
11000
00100
00011
Output: 3
'''

class Solution:
    # overwrite original grid
    def numIslands(self, grid: 'List[List[str]]') -> 'int':
        if not grid:
            return 0
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    count += 1
                self.dfs(grid, r, c)
        return count

    def dfs(self, grid: 'List[List[str]]', r: 'int', c: 'int'):
        if not (0 <= r < len(grid)) or not (0 <= c < len(grid[0])) or grid[r][c] == '0':
            return
        grid[r][c] = '0'
        self.dfs(grid, r - 1, c)
        self.dfs(grid, r + 1, c)
        self.dfs(grid, r, c - 1)
        self.dfs(grid, r, c + 1)
        return

        # add visited flags
    def numIslands_1(self, grid: 'List[List[str]]') -> 'int':
        if not grid:
            return 0
        count = 0
        r, c = len(grid), len(grid[0])
        visited = [[False for _ in range(c)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1' and not visited[i][j]:
                    count += 1
                self.dfs_1(grid, i, j, visited)
        return count

    def dfs_1(self, grid: 'List[List[str]]', i: 'int', j: 'int', visited: 'List[List[bool]]'):
        if not (0 <= i < len(grid)) or not (0 <= j < len(grid[0])) or grid[i][j] == '0' or visited[i][j]:
            return
        visited[i][j] = True
        self.dfs_1(grid, i - 1, j, visited)
        self.dfs_1(grid, i + 1, j, visited)
        self.dfs_1(grid, i, j - 1, visited)
        self.dfs_1(grid, i, j + 1, visited)
        return

    def numIslands_2(self, grid: 'List[List[str]]') -> 'int':
        if not grid:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs_2(grid, i, j)
        return count

    def dfs_2(self, grid: 'List[List[str]]', i: 'int', j: 'int'):
        grid[i][j] = '0'
        if i > 0 and grid[i - 1][j] == '1': self.dfs_2(grid, i - 1, j)
        if j > 0 and grid[i][j - 1] == '1': self.dfs_2(grid, i, j - 1)
        if i < len(grid) - 1 and grid[i + 1][j] == '1': self.dfs_2(grid, i + 1, j)
        if j < len(grid[i]) - 1 and grid[i][j + 1] == '1': self.dfs_2(grid, i, j + 1)


if __name__ == "__main__":
    a = Solution()
    grid = [['1', '1', '1', '1', '0'],
            ['1', '1', '0', '1', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '0', '0', '0']]
    print(a.numIslands(grid))
    grid = [['1', '1', '0', '0', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '1', '0', '0'],
            ['0', '0', '0', '1', '1']]
    print(a.numIslands(grid))

    grid = [['1', '1', '1', '1', '0'],
            ['1', '1', '0', '1', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '0', '0', '0']]
    print(a.numIslands_1(grid))
    print(a.numIslands_2(grid))
    grid = [['1', '1', '0', '0', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '1', '0', '0'],
            ['0', '0', '0', '1', '1']]
    print(a.numIslands_1(grid))
    print(a.numIslands_2(grid))