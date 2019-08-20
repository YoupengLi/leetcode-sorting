# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 22:00
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0173_BSTIterator.py
# @Software: PyCharm

'''
173. Binary Search Tree Iterator

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
Calling next() will return the next smallest number in the BST.

Example:
    7
   / \
  3  15
    /  \
   9   20
BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false

Note:
next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.inOrder(root)

    def inOrder(self, root):
        """
        :type root: TreeNode
        """
        if not root:
            return
        self.inOrder(root.left)
        self.stack.extend([root.val])
        self.inOrder(root.right)

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        if self.stack:
            return self.stack.pop(0)
        else:
            return

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        if len(self.stack) > 0:
            return True
        else:
            return False


class BSTIterator_1(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        if self.stack:
            node = self.stack[-1]
            res = node.val
            node = node.right
            self.stack.pop()
            while node:
                self.stack.append(node)
                node = node.left
            return res
        else:
            return

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return len(self.stack) >= 1

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

if __name__ == "__main__":
    '''
                7
               / \
              3  15
                /  \
               9   20
    '''
    t1 = TreeNode(7)
    t2 = TreeNode(3)
    t3 = TreeNode(15)
    t4 = TreeNode(9)
    t5 = TreeNode(20)

    t1.left = t2
    t1.right = t3
    t3.left = t4
    t3.right = t5

    root = t1
    a = BSTIterator(t1)
    print(a.next())
    print(a.next())
    print(a.hasNext())
    print(a.next())
    print(a.hasNext())
    print(a.next())
    print(a.hasNext())
    print(a.next())
    print(a.hasNext())

    t1 = TreeNode(7)
    t2 = TreeNode(3)
    t3 = TreeNode(15)
    t4 = TreeNode(9)
    t5 = TreeNode(20)

    t1.left = t2
    t1.right = t3
    t3.left = t4
    t3.right = t5

    root = t1
    a = BSTIterator_1(t1)
    print(a.next())
    print(a.next())
    print(a.hasNext())
    print(a.next())
    print(a.hasNext())
    print(a.next())
    print(a.hasNext())
    print(a.next())
    print(a.hasNext())

    t11 = None
    a = BSTIterator(t11)
    print(a.next())

    t11 = None
    a = BSTIterator_1(t11)
    print(a.next())