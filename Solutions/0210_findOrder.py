# -*- coding: utf-8 -*-
# @Time    : 2019/9/3 20:54
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0210_findOrder.py
# @Software: PyCharm

'''
210. Course Schedule II

There are a total of n courses you have to take, labeled from 0 to n-1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs,
return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them.
If it is impossible to finish all courses, return an empty array.

Example 1:
Input: 2, [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished
             course 0. So the correct course order is [0,1] .

Example 2:
Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices.
Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
'''

import collections

class Solution(object):
    # BFS: from the front to the end
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        forward = {i: set() for i in range(numCourses)}
        backward = collections.defaultdict(set)
        for i, j in prerequisites:
            forward[i].add(j)
            backward[j].add(i)
        # queue stores the courses which have no prerequisites
        queue = collections.deque([node for node in forward if len(forward[node]) == 0])
        count, res = 0, []
        while queue:
            node = queue.popleft()
            res.append(node)
            count += 1
            for neigh in backward[node]:
                forward[neigh].remove(node)
                if len(forward[neigh]) == 0:
                    queue.append(neigh)
        return res if count == numCourses else []

    # DFS: from the end to the front
    def findOrder_1(self, numCourses, prerequisites):
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
        count, res = 0, []
        while stack:
            node = stack.pop()
            res.append(node)
            count += 1
            for neigh in backward[node]:
                forward[neigh].remove(node)
                if len(forward[neigh]) == 0:
                    stack.append(neigh)
        return res if count == numCourses else []

if __name__ == "__main__":
    a = Solution()
    numCourses, prerequisites = 2, [[1, 0]]
    print(a.findOrder(numCourses, prerequisites))
    print(a.findOrder_1(numCourses, prerequisites))
    numCourses, prerequisites = 4, [[1, 0], [2, 0], [3, 1], [3, 2]]
    print(a.findOrder(numCourses, prerequisites))
    print(a.findOrder_1(numCourses, prerequisites))