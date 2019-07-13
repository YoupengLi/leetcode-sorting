# -*- coding: utf-8 -*-
# @Time    : 2019/7/12 14:02
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0133_cloneGraph.py
# @Software: PyCharm

'''
133. Clone Graph

Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.
Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

Example:
    1———————————2
    |           |
    |           |
    |           |
    4———————————3
Input:
{"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},
{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}

Explanation:
Node 1's value is 1, and it has two neighbors: Node 2 and 4.
Node 2's value is 2, and it has two neighbors: Node 1 and 3.
Node 3's value is 3, and it has two neighbors: Node 2 and 4.
Node 4's value is 4, and it has two neighbors: Node 1 and 3.

Note:
The number of nodes will be between 1 and 100.
The undirected graph is a simple graph, which means no repeated edges and no self-loops in the graph.
Since the graph is undirected, if node p has node q as neighbor, then node q must have node p as neighbor too.
You must return the copy of the given node as a reference to the cloned graph.
'''

from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # BFS iteratively
        if not node:
            return
        nodeCopy = Node(node.val, [])
        dic = {node: nodeCopy}
        queue = deque([node])
        while queue:
            node = queue.popleft()
            for neighbor in node.neighbors:
                if neighbor not in dic:  # neighbor is not visited
                    neighborCopy = Node(neighbor.val, [])
                    dic[neighbor] = neighborCopy
                    dic[node].neighbors.append(neighborCopy)
                    queue.append(neighbor)
                else:
                    dic[node].neighbors.append(dic[neighbor])
        return nodeCopy

    def cloneGraph_1(self, node: 'Node') -> 'Node':
        # DFS iteratively
        if not node:
            return
        nodeCopy = Node(node.val, [])
        dic = {node: nodeCopy}
        stack = [node]
        while stack:
            node = stack.pop()
            for neighbor in node.neighbors:
                if neighbor not in dic:
                    neighborCopy = Node(neighbor.val, [])
                    dic[neighbor] = neighborCopy
                    dic[node].neighbors.append(neighborCopy)
                    stack.append(neighbor)
                else:
                    dic[node].neighbors.append(dic[neighbor])
        return nodeCopy

    def cloneGraph_2(self, node: 'Node') -> 'Node':
        # DFS recursively
        if not node:
            return
        nodeCopy = Node(node.val, [])
        dic = {node: nodeCopy}
        self.dfs(node, dic)
        return nodeCopy

    def dfs(self, node: 'Node', dic: 'dict{Node}'):
        for neighbor in node.neighbors:
            if neighbor not in dic:
                neighborCopy = Node(neighbor.val, [])
                dic[neighbor] = neighborCopy
                dic[node].neighbors.append(neighborCopy)
                self.dfs(neighbor, dic)
            else:
                dic[node].neighbors.append(dic[neighbor])

    def cloneGraph_3(self, node: 'Node') -> 'Node':
        if not node:
            return node
        root = Node(node.val, [])
        stack = [node]
        visit = {}
        visit[node.val] = root
        while stack:
            top = stack.pop()
            for n in top.neighbors:
                if n.val not in visit:
                    stack.append(n)
                    visit[n.val] = Node(n.val, [])
                visit[top.val].neighbors.append(visit[n.val])
        return root

if __name__ == "__main__":
    '''
    1———————————2
    |           |
    |           |
    |           |
    4———————————3
    '''
    a = Solution()
    t1 = Node(1, [])
    t2 = Node(2, [])
    t3 = Node(3, [])
    t4 = Node(4, [])
    t1.neighbors += [t2, t4]
    t2.neighbors += [t1, t3]
    t3.neighbors += [t2, t4]
    t4.neighbors += [t1, t3]
    '''
    t1.neighbors.append(t2)
    t1.neighbors.append(t4)
    t2.neighbors.append(t1)
    t2.neighbors.append(t3)
    t3.neighbors.append(t2)
    t3.neighbors.append(t4)
    t4.neighbors.append(t1)
    t4.neighbors.append(t3)
    '''
    res = a.cloneGraph(t1)
    res = a.cloneGraph_1(t1)
    res = a.cloneGraph_2(t1)
    res = a.cloneGraph_3(t1)
    print(res)