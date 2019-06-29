# -*- coding: utf-8 -*-
# @Time    : 2019/6/28 18:10
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0114_flatten.py
# @Software: PyCharm

'''
114. Flatten Binary Tree to Linked List

Given a binary tree, flatten it to a linked list in-place.
For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root: 'TreeNode') -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        while root:
            if root.left:
                self.flatten(root.left)
                node1 = root.left
                while node1.right:
                    node1 = node1.right
                node2 = root.right
                root.right = root.left
                root.left = None
                node1.right = node2
            root = root.right

    def flatten_1(self, root: 'TreeNode') -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.flatten_1(root.left)
        self.flatten_1(root.right)
        if root.left:
            temp = root.right
            root.right = root.left
            root.left = None
            while root.right:
                root = root.right
            root.right = temp

    def flatten_2(self, root: 'TreeNode') -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        while stack or root:
            if root:
                if root.right:
                    stack.append(root.right)
                if root.left:
                    root.right = root.left
                    root.left = None
                elif stack:
                    temp = stack.pop()
                    root.right = temp
                root = root.right

    def flatten_3(self, root: 'TreeNode') -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev = None

        def dfs(node: 'TreeNode') -> None:
            if not node:
                return

            dfs(node.right)
            dfs(node.left)

            node.right = self.prev
            node.left = None
            self.prev = node

        dfs(root)

if __name__ == "__main__":
    '''
        1
       / \
      2   5
     / \   \
    3   4   6
    '''
    a = Solution()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(5)
    t4 = TreeNode(3)
    t5 = TreeNode(4)
    t6 = TreeNode(6)

    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.right = t6


    root = t1
    print(a.flatten(root))
    print(a.flatten_1(root))
    print(a.flatten_2(root))
    print(a.flatten_3(root))
