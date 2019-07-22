# -*- coding: utf-8 -*-
# @Time    : 2019/7/21 10:59
# @Author  : Youpeng Li
# @Site    : 
# @File    : 1129_shortestAlternatingPaths.py
# @Software: PyCharm

'''
1129. Shortest Path with Alternating Colors

Consider a directed graph, with nodes labelled 0, 1, ..., n-1.
In this graph, each edge is either red or blue, and there could be self-edges or parallel edges.
Each [i, j] in red_edges denotes a red directed edge from node i to node j.
Similarly, each [i, j] in blue_edges denotes a blue directed edge from node i to node j.

Return an array answer of length n, where each answer[X] is the length of the shortest path from node 0 to node X
such that the edge colors alternate along the path (or -1 if such a path doesn't exist).

Example 1:
Input: n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
Output: [0,1,-1]

Example 2:
Input: n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]
Output: [0,1,-1]

Example 3:
Input: n = 3, red_edges = [[1,0]], blue_edges = [[2,1]]
Output: [0,-1,-1]

Example 4:
Input: n = 3, red_edges = [[0,1]], blue_edges = [[1,2]]
Output: [0,1,2]

Example 5:
Input: n = 3, red_edges = [[0,1],[0,2]], blue_edges = [[1,0]]
Output: [0,1,1]

Constraints:
1 <= n <= 100
red_edges.length <= 400
blue_edges.length <= 400
red_edges[i].length == blue_edges[i].length == 2
0 <= red_edges[i][j], blue_edges[i][j] < n
'''

from collections import defaultdict, deque
import math

class Solution:
    def shortestAlternatingPaths(self, n: 'int', red_edges: 'List[List[int]]', blue_edges: 'List[List[int]]') -> 'List[int]':
        graph = defaultdict(lambda: defaultdict(set))
        red, blue = 0, 1
        for st, end in red_edges:
            graph[st][red].add(end)
        for st, end in blue_edges:
            graph[st][blue].add(end)
        res = [math.inf] * n

        q = deque([(0, red), (0, blue)])
        level = -1
        while q:
            level += 1
            size = len(q)
            for i in range(size):
                node, color = q.popleft()
                opp_color = color ^ 1
                res[node] = min(level, res[node])
                neighbors = graph[node][opp_color]
                for child in list(neighbors):
                    graph[node][opp_color].remove(child)
                    q.append((child, opp_color))
        return [r if r != math.inf else -1 for r in res]

    def shortestAlternatingPaths_1(self, n: 'int', red_edges: 'List[List[int]]', blue_edges: 'List[List[int]]') -> 'List[int]':
        reds = defaultdict(list)
        blues = defaultdict(list)
        for i, j in red_edges:
            reds[i].append(j)
        for i, j in blue_edges:
            blues[i].append(j)
        # print(reds, blues)
        frontier = deque([(v, 'r') for v in reds[0]] + [(v, 'b') for v in blues[0]])
        # print(frontier)
        res = [-1] * n
        res[0] = 0
        step = 0
        seen = {(0, 'r'), (0, 'b')}
        for node, c in frontier:
            seen.add((node, c))
        while frontier:
            step += 1
            sz = len(frontier)
            for _ in range(sz):
                node, color = frontier.popleft()
                if res[node] == -1:
                    res[node] = step
                nei_lst = blues if color == 'r' else reds
                for nei in nei_lst[node]:
                    new_color = 'r' if color == 'b' else 'b'
                    if (nei, new_color) not in seen:
                        seen.add((nei, new_color))
                        frontier.append((nei, new_color))
        return res

if __name__ == "__main__":
    a = Solution()
    n = 3
    red_edges = [[0, 1], [1, 2]]
    blue_edges = []
    print(a.shortestAlternatingPaths(n, red_edges, blue_edges))
    print(a.shortestAlternatingPaths_1(n, red_edges, blue_edges))
    red_edges = [[0, 1]]
    blue_edges = [[2, 1]]
    print(a.shortestAlternatingPaths(n, red_edges, blue_edges))
    print(a.shortestAlternatingPaths_1(n, red_edges, blue_edges))
    red_edges = [[1, 0]]
    blue_edges = [[2, 1]]
    print(a.shortestAlternatingPaths(n, red_edges, blue_edges))
    print(a.shortestAlternatingPaths_1(n, red_edges, blue_edges))
    red_edges = [[0, 1]]
    blue_edges = [[1, 2]]
    print(a.shortestAlternatingPaths(n, red_edges, blue_edges))
    print(a.shortestAlternatingPaths_1(n, red_edges, blue_edges))
    red_edges = [[0, 1], [0, 2]]
    blue_edges = [[1, 0]]
    print(a.shortestAlternatingPaths(n, red_edges, blue_edges))
    print(a.shortestAlternatingPaths_1(n, red_edges, blue_edges))