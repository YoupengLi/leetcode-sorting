# -*- coding: utf-8 -*-
# @Time    : 2019/6/26 9:01
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0106_buildTree.py
# @Software: PyCharm

'''
106. Construct Binary Tree from Inorder and Postorder Traversal

Given inorder and postorder traversal of a tree, construct the binary tree.
Note:
You may assume that duplicates do not exist in the tree.

For example, given
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

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
    def buildTree(self, inorder: 'List[int]', postorder: 'List[int]') -> 'TreeNode':
        if postorder == []:
            return None
        val = postorder[-1]
        ind = inorder.index(val)
        lin = inorder[0:ind]
        rin = inorder[ind+1:]
        lpos = postorder[0:len(lin)]
        rpos = postorder[len(lin):-1]
        root = TreeNode(val)
        root.left = self.buildTree(lin, lpos)
        root.right = self.buildTree(rin, rpos)
        return root

    def buildTree_1(self, inorder: 'List[int]', postorder: 'List[int]') -> 'TreeNode':
        def helper(start, end):
            if start > end:
                return None
            value = postorder.pop()
            root = TreeNode(value)
            index = hashmap[value]
            root.right = helper(index+1, end)
            root.left = helper(start, index-1)
            return root

        hashmap = {key: val for val, key in enumerate(inorder)}
        return helper(0, len(inorder)-1)

    def buildTree_2(self, inorder: 'List[int]', postorder: 'List[int]') -> 'TreeNode':
        def build(stop):
            if inorder and inorder[-1] != stop:
                root = TreeNode(postorder.pop())
                root.right = build(root.val)
                inorder.pop()
                root.left = build(stop)
                return root
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
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    res = a.buildTree(inorder, postorder)
    res = a.buildTree_1(inorder, postorder)
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    res = a.buildTree_2(inorder, postorder)
    print(res)