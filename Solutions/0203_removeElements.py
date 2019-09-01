# -*- coding: utf-8 -*-
# @Time    : 2019/9/1 8:07
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0203_removeElements.py
# @Software: PyCharm

'''
203. Remove Linked List Elements

Remove all elements from a linked list of integers that have value val.

Example:
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = pre = ListNode(0)
        while head:
            if head.val != val:
                pre.next = ListNode(head.val)
                pre = pre.next
            head = head.next
        return dummy.next

    # in-place
    def removeElements_1(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = pre = ListNode(0)
        dummy.next = head
        while head:
            if head.val == val:
                pre.next = head.next
            else:
                pre = pre.next
            head = head.next
        return dummy.next

if __name__ == "__main__":
    a = Solution()

    '''
     1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6

    '''
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(6)
    l4 = ListNode(3)
    l5 = ListNode(4)
    l6 = ListNode(5)
    l7 = ListNode(6)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    l5.next = l6
    l6.next = l7
    head = l1
    head = a.removeElements(head, 6)
    res = []
    while head:
        res += [head.val]
        head = head.next
    print(res)

    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(6)
    l4 = ListNode(3)
    l5 = ListNode(4)
    l6 = ListNode(5)
    l7 = ListNode(6)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    l5.next = l6
    l6.next = l7
    head = l1
    head = a.removeElements_1(head, 6)
    res = []
    while head:
        res += [head.val]
        head = head.next
    print(res)