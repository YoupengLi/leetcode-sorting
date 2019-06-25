# -*- coding: utf-8 -*-
# @Time    : 2019/6/24 21:40
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0101_isSymmetric.py
# @Software: PyCharm

'''
101. Symmetric Tree

Given a binary tree, check whether it is a mirror of itself
(ie, symmetric around its center).
For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3

Note:
Bonus points if you could solve it both recursively and iteratively.
'''

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: 'TreeNode') -> 'bool':
        return self.isMirror(root, root)

    def isMirror(self, p: 'TreeNode', q: 'TreeNode') -> 'bool':
        # p and q are both None
        if not p and not q:
            return True
        # one of p and q is None
        if not q or not p:
            return False
        if p.val != q.val:
            return False
        return self.isMirror(p.left, q.right) and self.isMirror(p.right, q.left)

    def isSymmetric_1(self, root: 'TreeNode') -> 'bool':
        if not root:
            return True
        stack = deque([root.left, root.right])
        while stack:
            left = stack.pop()
            right = stack.pop()
            if not left and not right:
                continue
            elif not left or not right:
                return False
            if left.val != right.val:
                return False
            stack.append(left.left)
            stack.append(right.right)
            stack.append(left.right)
            stack.append(right.left)
        return True

if __name__ == "__main__":
    '''
            1
           / \
          2   2
         / \ / \
        3  4 4  3
    '''
    a = Solution()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(2)
    t4 = TreeNode(3)
    t5 = TreeNode(4)
    t6 = TreeNode(4)
    t7 = TreeNode(3)

    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.left = t6
    t3.right = t7
    root = t1

    print(a.isSymmetric(root))
    print(a.isSymmetric_1(root))

    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(2)
    t4 = TreeNode(3)
    t5 = TreeNode(3)

    t1.left = t2
    t1.right = t3
    t2.right = t4
    t3.right = t5
    root = t1

    print(a.isSymmetric(root))
    print(a.isSymmetric_1(root))