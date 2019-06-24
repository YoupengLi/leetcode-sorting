# -*- coding: utf-8 -*-
# @Time    : 2019/6/19 16:05
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0099_recoverTree.py
# @Software: PyCharm

'''
99. Recover Binary Search Tree

Two elements of a binary search tree (BST) are swapped by mistake.
Recover the tree without changing its structure.

Example 1:
Input: [1,3,null,null,2]
   1
  /
 3
  \
   2
Output: [3,1,null,null,2]
   3
  /
 1
  \
   2

Example 2:
Input: [3,1,4,null,null,2]
  3
 / \
1   4
   /
  2
Output: [2,1,4,null,null,3]
  2
 / \
1   4
   /
  3

Follow up:
A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverTree(self, root: 'TreeNode') -> 'None':
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        list_nums = []
        list_root = []
        self.inorder(root, list_nums, list_root)
        list_nums.sort()
        for i, root in enumerate(list_root):
            root.val = list_nums[i]

    def inorder(self, root: 'TreeNode', list_num: 'list[int]', list_root: 'list[int]') -> 'None':
        if root:
            self.inorder(root.left, list_num, list_root)
            list_num.append(root.val)
            list_root.append(root)
            self.inorder(root.right, list_num, list_root)

    def recoverTree_1(self, root: TreeNode) -> None:
        self.n1 = TreeNode(None)
        self.n2 = TreeNode(None)
        self.pre = TreeNode(None)
        self.inorderT(root)
        self.n1.val, self.n2.val = self.n2.val, self.n1.val

    def inorderT(self, root: 'TreeNode') -> 'None':
        if root:
            self.inorderT(root.left)
            if self.pre and root.val != None and self.pre.val != None and root.val < self.pre.val:
                self.n2 = root
                if self.n1.val == None:
                    self.n1 = self.pre
            self.pre = root
            self.inorderT(root.right)

if __name__ == "__main__":
    '''
       1
      /
     3
      \
       2
    '''
    a = Solution()
    t1 = TreeNode(1)
    t2 = TreeNode(3)
    t3 = TreeNode(2)

    t1.left = t2
    t2.right = t3
    root = t1
    print(a.recoverTree(root))

    t1 = TreeNode(1)
    t2 = TreeNode(3)
    t3 = TreeNode(2)

    t1.left = t2
    t2.right = t3
    root = t1
    print(a.recoverTree_1(root))
    '''
      3
     / \
    1   4
       /
      2
    '''
    t11 = TreeNode(3)
    t12 = TreeNode(1)
    t13 = TreeNode(4)
    t14 = TreeNode(2)

    t11.left = t12
    t11.right = t13
    t13.left = t14
    root = t11
    print(a.recoverTree(root))

    t11 = TreeNode(3)
    t12 = TreeNode(1)
    t13 = TreeNode(4)
    t14 = TreeNode(2)

    t11.left = t12
    t11.right = t13
    t13.left = t14
    root = t11
    print(a.recoverTree_1(root))