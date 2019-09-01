# -*- coding: utf-8 -*-
# @Time    : 2019/9/1 16:47
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0207_canFinish.py
# @Software: PyCharm

'''
207. Course Schedule

There are a total of n courses you have to take, labeled from 0 to n-1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:
Input: 2, [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices.
Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
'''

import collections

class Solution(object):
    # BFS: from the front to the end
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        forward = {i: set() for i in range(numCourses)}
        backward = collections.defaultdict(set)
        for i, j in prerequisites:
            forward[i].add(j)
            backward[j].add(i)
        queue = collections.deque([node for node in range(numCourses) if not backward[node]])
        count = 0
        while queue:
            node = queue.popleft()
            count += 1
            for neigh in forward[node]:
                backward[neigh].remove(node)
                if not backward[neigh]:
                    queue.append(neigh)
        return count == numCourses

    # BFS: from the end to the front
    def canFinish_1(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        forward = {i: set() for i in range(numCourses)}
        backward = collections.defaultdict(set)
        for i, j in prerequisites:
            forward[i].add(j)
            backward[j].add(i)
        queue = collections.deque([node for node in forward if len(forward[node]) == 0])
        while queue:
            node = queue.popleft()
            for neigh in backward[node]:
                forward[neigh].remove(node)
                if len(forward[neigh]) == 0:
                    queue.append(neigh)
            forward.pop(node)
        return not forward  # if there is cycle, forward won't be None

    # DFS: from the front to the end
    def canFinish_2(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        forward = {i: set() for i in range(numCourses)}
        backward = collections.defaultdict(set)
        for i, j in prerequisites:
            forward[i].add(j)
            backward[j].add(i)
        stack = [node for node in range(numCourses) if not backward[node]]
        while stack:
            node = stack.pop()
            for neigh in forward[node]:
                backward[neigh].remove(node)
                if not backward[neigh]:
                    stack.append(neigh)
            backward.pop(node)
        return not backward

    # DFS: from the end to the front
    def canFinish_3(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        forward = {i: set() for i in range(numCourses)}
        backward = collections.defaultdict(set)
        for i, j in prerequisites:
            forward[i].add(j)
            backward[j].add(i)
        stack = [node for node in forward if len(forward[node]) == 0]
        while stack:
            node = stack.pop()
            for neigh in backward[node]:
                forward[neigh].remove(node)
                if len(forward[neigh]) == 0:
                    stack.append(neigh)
            forward.pop(node)
        return not forward

    def canFinish_4(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        # 0 = Unknown, 1 = visiting, 2 = visited
        visited = [0] * numCourses
        for i in range(numCourses):
            if not self.dfs(graph, visited, i):
                return False
        return True

    # Can we add node i to visited successfully?
    def dfs(self, graph, visited, i):
        if visited[i] == 1: return False
        if visited[i] == 2: return True
        visited[i] = 1
        for j in graph[i]:
            if not self.dfs(graph, visited, j):
                return False
        visited[i] = 2
        return True


if __name__ == "__main__":
    a = Solution()
    numCourses = 2
    prerequisites = [[1, 0]]
    print(a.canFinish(numCourses, prerequisites))
    print(a.canFinish_1(numCourses, prerequisites))
    print(a.canFinish_2(numCourses, prerequisites))
    print(a.canFinish_3(numCourses, prerequisites))
    print(a.canFinish_4(numCourses, prerequisites))
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]
    print(a.canFinish(numCourses, prerequisites))
    print(a.canFinish_1(numCourses, prerequisites))
    print(a.canFinish_2(numCourses, prerequisites))
    print(a.canFinish_3(numCourses, prerequisites))
    print(a.canFinish_4(numCourses, prerequisites))
    numCourses = 4
    prerequisites = [[1, 2], [2, 0], [2, 3]]
    print(a.canFinish(numCourses, prerequisites))
    print(a.canFinish_1(numCourses, prerequisites))
    print(a.canFinish_2(numCourses, prerequisites))
    print(a.canFinish_3(numCourses, prerequisites))
    print(a.canFinish_4(numCourses, prerequisites))
    numCourses = 4
    prerequisites = [[1, 2], [2, 0], [2, 3]]
    print(a.canFinish(numCourses, prerequisites))
    print(a.canFinish_1(numCourses, prerequisites))
    print(a.canFinish_2(numCourses, prerequisites))
    print(a.canFinish_3(numCourses, prerequisites))
    print(a.canFinish_4(numCourses, prerequisites))