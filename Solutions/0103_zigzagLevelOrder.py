# -*- coding: utf-8 -*-
# @Time    : 2019/6/25 12:46
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0103_zigzagLevelOrder.py
# @Software: PyCharm

'''
103. Binary Tree Zigzag Level Order Traversal

Given a binary tree, return the zigzag level order traversal of its nodes' values.
(ie, from left to right, then right to left for the next level and alternate between).
For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
'''

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: 'TreeNode') -> 'List[List[int]]':
        if not root:
            return []
        res = []
        q = deque([root])
        ind = 0
        while q:
            if ind % 2 == 0:
                res.append([node.val for node in q])
            else:
                res.append(list(reversed([node.val for node in q])))
            ind += 1
            len_q = len(q)
            for _ in range(len_q):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res

    def zigzagLevelOrder_1(self, root: 'TreeNode') -> 'List[List[int]]':
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
            if len(res) % 2 == 1:
                tmp.reverse()
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

    print(a.zigzagLevelOrder(root))
    print(a.zigzagLevelOrder_1(root))

    '''
            1
           / \
          2   3
         /     \
        4       5
    '''
    a = Solution()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)

    t1.left = t2
    t1.right = t3
    t2.left = t4
    t3.right = t5

    root = t1

    print(a.zigzagLevelOrder(root))
    print(a.zigzagLevelOrder_1(root))