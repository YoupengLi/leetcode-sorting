# -*- coding: utf-8 -*-
# @Time    : 2019/6/25 15:54
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0105_buildTree.py
# @Software: PyCharm

'''
105. Construct Binary Tree from Preorder and Inorder Traversal

Given preorder and inorder traversal of a tree, construct the binary tree.
Note:
You may assume that duplicates do not exist in the tree.

For example, given
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

Return the following binary tree:
    3
   / \
  9  20
    /  \
   15   7
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: 'List[int]', inorder: 'List[int]') -> 'TreeNode':
        if preorder == []:
            return None
        val = preorder[0]
        ind = inorder.index(val)
        lin = inorder[0:ind]
        rin = inorder[ind+1:]
        lpre = preorder[1:1+len(lin)]
        rpre = preorder[1+len(lin):]
        root = TreeNode(val)
        root.left = self.buildTree(lpre, lin)
        root.right = self.buildTree(rpre, rin)
        return root

    def buildTree_1(self, preorder: 'List[int]', inorder: 'List[int]') -> 'TreeNode':
        def helper(start, end):
            if start == end:
                return None
            nonlocal pre_index
            value = preorder[pre_index]
            root = TreeNode(value)
            pre_index += 1

            index = hashmap[value]

            root.left = helper(start, index)
            root.right = helper(index + 1, end)
            return root

        hashmap = {key: val for val, key in enumerate(inorder)}
        pre_index = 0
        return helper(0, len(inorder))

    def buildTree_2(self, preorder: 'List[int]', inorder: 'List[int]') -> 'TreeNode':
        def build(stop):
            if inorder and inorder[-1] != stop:
                root = TreeNode(preorder.pop())
                root.left = build(root.val)
                inorder.pop()
                root.right = build(stop)
                return root

        preorder.reverse()
        inorder.reverse()
        return build(None)

if __name__ == "__main__":
    '''
            3
           / \
          9  20
            /  \
           15   7
    '''
    a = Solution()
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    res = a.buildTree(preorder, inorder)
    res = a.buildTree_1(preorder, inorder)
    res = a.buildTree_2(preorder, inorder)