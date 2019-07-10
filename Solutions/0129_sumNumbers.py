# -*- coding: utf-8 -*-
# @Time    : 2019/7/10 21:59
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0129_sumNumbers.py
# @Software: PyCharm

'''
129. Sum Root to Leaf Numbers

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
An example is the root-to-leaf path 1->2->3 which represents the number 123.
Find the total sum of all root-to-leaf numbers.
Note: A leaf is a node with no children.

Example:
Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

Example 2:
Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
'''

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root: 'TreeNode') -> 'int':
        # dfs + stack
        if not root:
            return 0
        stack, res = [(root, root.val)], 0
        while stack:
            node, val = stack.pop()
            if node:
                if not node.left and not node.right:
                    res += val
                if node.left:
                    stack.append((node.left, val * 10 + node.left.val))
                if node.right:
                    stack.append((node.right, val * 10 + node.right.val))
        return res

    def sumNumbers_1(self, root: 'TreeNode') -> 'int':
        # bfs + queue
        if not root:
            return 0
        queue, res = deque([(root, root.val)]), 0
        while queue:
            node, val = queue.popleft()
            if node:
                if not node.left and not node.right:
                    res += val
                if node.left:
                    queue.append((node.left, val * 10 + node.left.val))
                if node.right:
                    queue.append((node.right, val * 10 + node.right.val))
        return res

    def sumNumbers_2(self, root: 'TreeNode') -> 'int':
        # recursively
        self.res = 0
        self.dfs(root, 0)
        return self.res

    def dfs(self, root: 'TreeNode', val: 'int') -> 'None':
        if root:
            # if not root.left and not root.right:
            #    self.res += value*10 + root.val
            self.dfs(root.left, val * 10 + root.val)
            # if not root.left and not root.right:
            #    self.res += value*10 + root.val
            self.dfs(root.right, val * 10 + root.val)
            if not root.left and not root.right:
                self.res += val * 10 + root.val

    def sumNumbers_3(self, root: 'TreeNode') -> 'int':
        if not root:
            return 0
        self.res = 0

        def dfs(root: 'TreeNode', val: 'int') -> 'None':
            val = val * 10 + root.val
            if not root.left and not root.right:
                self.res += val
                return
            if root.left:
                dfs(root.left, val)
            if root.right:
                dfs(root.right, val)

        dfs(root, 0)
        return self.res

if __name__ == "__main__":
    '''
          4
         / \
        9   0
       / \
      5   1
    '''
    a = Solution()
    t1 = TreeNode(4)
    t2 = TreeNode(9)
    t3 = TreeNode(0)
    t4 = TreeNode(5)
    t5 = TreeNode(1)

    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5

    root = t1
    print(a.sumNumbers(root))
    print(a.sumNumbers_1(root))
    print(a.sumNumbers_2(root))
    print(a.sumNumbers_3(root))