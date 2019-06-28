# -*- coding: utf-8 -*-
# @Time    : 2019/6/28 11:20
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0111_minDepth.py
# @Software: PyCharm

'''
111. Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.

Example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: 'TreeNode') -> 'int':
        if not root:
            return 0
        if None in [root.left, root.right]:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

    def minDepth_1(self, root: 'TreeNode') -> 'int':
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if root.left and not root.right:
            return 1 + self.minDepth(root.left)
        if root.right and not root.left:
            return 1 + self.minDepth(root.right)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

    def minDepth_2(self, root: 'TreeNode') -> 'int':
        if not root: return 0
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        return (min(l, r) or max(l, r)) + 1

    def minDepth_3(self, root: 'TreeNode') -> 'int':
        if not root:
            return 0
        depth = 1
        stack = [root]
        while stack:
            next_level = []
            for node in stack:
                if node.left or node.right:
                    if node.left:
                        next_level.append(node.left)
                    if node.right:
                        next_level.append(node.right)
                else:
                    return depth
            stack = next_level
            depth += 1

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
    print(a.minDepth(root))
    print(a.minDepth_1(root))
    print(a.minDepth_2(root))
    print(a.minDepth_3(root))