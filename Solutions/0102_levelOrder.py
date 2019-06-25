# -*- coding: utf-8 -*-
# @Time    : 2019/6/25 11:25
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0102_levelOrder.py
# @Software: PyCharm

'''
102. Binary Tree Level Order Traversal

Given a binary tree, return the level order traversal of its nodes' values.
(ie, from left to right, level by level).
For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: 'TreeNode') -> 'List[List[int]]':
        res = []
        queue = [(root, 0)]
        for node, level in queue:
            if node:
                if level >= len(res):
                    res.append([])
                res[level].append(node.val)
                if node.left:
                    queue.append((node.left, level+1))
                if node.right:
                    queue.append((node.right, level+1))
        return res

    def levelOrder_1(self, root: 'TreeNode') -> 'List[List[int]]':
        if not root:
            return []
        res, queue = [], [root]
        while queue:
            tmp, new = [], []
            for node in queue:
                tmp.append(node.val)
                if node.left:
                    new.append(node.left)
                if node.right:
                    new.append(node.right)
            res.append(tmp)
            queue = new
        return res

if __name__ == "__main__":
    '''
            3
           / \
          9  20
            /  \
           15   7
    '''
    a = Solution()
    t1 = TreeNode(3)
    t2 = TreeNode(9)
    t3 = TreeNode(20)
    t4 = TreeNode(15)
    t5 = TreeNode(7)

    t1.left = t2
    t1.right = t3
    t3.left = t4
    t3.right = t5

    root = t1

    print(a.levelOrder(root))
    print(a.levelOrder_1(root))