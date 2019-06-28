# -*- coding: utf-8 -*-
# @Time    : 2019/6/28 8:33
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0109_sortedListToBST.py
# @Software: PyCharm

'''
109. Convert Sorted List to Binary Search Tree

Given a singly linked list where elements are sorted in ascending order,
convert it to a height balanced BST.
For this problem, a height-balanced binary tree is defined as a binary tree
in which the depth of the two subtrees of every node never differ by more than 1.

Example:
Given the sorted linked list: [-10,-3,0,5,9],
One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
      0
     / \
   -3   9
   /   /
 -10  5
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head: 'ListNode') -> 'TreeNode':
        # If the head doesn't exist, then the linked list is empty
        if not head:
            return None

        # Find the middle element for the list.
        mid = self.findMiddle(head)

        # The mid becomes the root of the BST.
        node = TreeNode(mid.val)

        # Base case when there is just one element in the linked list
        if head == mid:
            return node

        # Recursively form balanced BSTs using the left and right halves of the original list.
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)
        return node

    def findMiddle(self, head: 'ListNode') -> 'ListNode':
        # The pointer used to disconnect the left half from the mid node.
        prevPtr = None
        slowPtr = head
        fastPtr = head

        # Iterate until fastPr doesn't reach the end of the linked list.
        while fastPtr and fastPtr.next:
            prevPtr = slowPtr
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next

        # Handling the case when slowPtr was equal to head.
        if prevPtr:
            prevPtr.next = None

        return slowPtr

    def sortedListToBST_1(self, head: 'ListNode') -> 'TreeNode':
        nums = self.mapListToValues(head)
        if not nums:
            return None
        return self.sortedArrayToBST(nums)

    # Convert the given linked list to an array
    def mapListToValues(self, head: 'ListNode') -> 'List[int]':
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        return vals

    def sortedArrayToBST(self, nums: 'List[int]') -> 'TreeNode':
        if not nums:
            return None
        mid = (len(nums)-1) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root

    def sortedListToBST_2(self, head: 'ListNode') -> 'TreeNode':
        nums = []
        while (head):
            nums.append(head.val)
            head = head.next
        return self.helper(nums, 0, len(nums)-1)

    def helper(self, nums: 'List[int]', l: 'int', r: 'int') -> 'TreeNode':
        if l > r:
            return None
        if l == r:
            return TreeNode(nums[l])
        mid = (l + r) // 2
        root = TreeNode(nums[mid])
        root.left = self.helper(nums, l, mid - 1)
        root.right = self.helper(nums, mid + 1, r)
        return root

if __name__ == "__main__":
    '''
    list1: -10->-3->0->5->9
    '''
    a = Solution()
    t1 = ListNode(-10)
    t2 = ListNode(-3)
    t3 = ListNode(0)
    t4 = ListNode(5)
    t5 = ListNode(9)

    t1.next = t2
    t2.next = t3
    t3.next = t4
    t4.next = t5

    head = t1

    res = a.sortedListToBST(head)
    print(res)

    t1 = ListNode(-10)
    t2 = ListNode(-3)
    t3 = ListNode(0)
    t4 = ListNode(5)
    t5 = ListNode(9)

    t1.next = t2
    t2.next = t3
    t3.next = t4
    t4.next = t5

    head = t1
    res = a.sortedListToBST_1(head)
    print(res)

    t1 = ListNode(-10)
    t2 = ListNode(-3)
    t3 = ListNode(0)
    t4 = ListNode(5)
    t5 = ListNode(9)

    t1.next = t2
    t2.next = t3
    t3.next = t4
    t4.next = t5

    head = t1
    res = a.sortedListToBST_2(head)
    print(res)