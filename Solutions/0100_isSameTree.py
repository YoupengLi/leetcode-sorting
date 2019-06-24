# -*- coding: utf-8 -*-
# @Time    : 2019/6/24 21:09
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0100_isSameTree.py
# @Software: PyCharm

'''
100. Same Tree

Given two binary trees, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical
and the nodes have the same value.

Example 1:
Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]
Output: true

Example 2:
Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]
Output: false

Example 3:
Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]
Output: false
'''

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: 'TreeNode', q: 'TreeNode') -> 'bool':
        # p and q are both None
        if not p and not q:
            return True
        # one of p and q is None
        if not q or not p:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)

    def isSameTree_1(self, p: 'TreeNode', q: 'TreeNode') -> 'bool':
        def check(p: 'TreeNode', q: 'TreeNode') -> 'bool':
            # if both are None
            if not p and not q:
                return True
            # one of p and q is None
            if not q or not p:
                return False
            if p.val != q.val:
                return False
            return True

        deq = deque([(p, q), ])
        while deq:
            p, q = deq.popleft()
            if not check(p, q):
                return False

            if p or q:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))

        return True

if __name__ == "__main__":
    '''
           1         1
          / \       / \
         2   1     1   2
    '''
    a = Solution()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(1)

    t1.left = t2
    t1.right = t3
    root1 = t1

    t11 = TreeNode(1)
    t12 = TreeNode(1)
    t13 = TreeNode(2)

    t11.left = t12
    t11.right = t13
    root2 = t11

    print(a.isSameTree(root1, root2))
    print(a.isSameTree_1(root1, root2))