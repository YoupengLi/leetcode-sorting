# -*- coding: utf-8 -*-
# @Time    : 2019/6/2 22:15
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0083_deleteDuplicates.py
# @Software: PyCharm

'''
83. Remove Duplicates from Sorted List

Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:
Input: 1->1->2
Output: 1->2

Example 2:
Input: 1->1->2->3->3
Output: 1->2->3
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: 'ListNode') -> 'ListNode':
        if not head or not head.next:
            return head
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head

    def deleteDuplicates_1(self, head: 'ListNode') -> 'ListNode':
        if not head or not head.next:
            return head
        pt = head
        pt_n = head.next
        while pt_n:
            if pt.val == pt_n.val:
                pt.next = pt_n.next
                pt_n = pt_n.next
            else:
                pt = pt.next
                pt_n = pt_n.next
        return head

if __name__ == "__main__":
    '''
    list1: 1->1->2->3->3
    '''
    a = Solution()
    t1 = ListNode(1)
    t2 = ListNode(1)
    t3 = ListNode(2)
    t4 = ListNode(3)
    t5 = ListNode(3)

    t1.next = t2
    t2.next = t3
    t3.next = t4
    t4.next = t5

    head = t1

    head = a.deleteDuplicates(head)
    print(head)

    t1 = ListNode(1)
    t2 = ListNode(1)
    t3 = ListNode(2)
    t4 = ListNode(3)
    t5 = ListNode(3)

    t1.next = t2
    t2.next = t3
    t3.next = t4
    t4.next = t5

    head = t1

    head = a.deleteDuplicates_1(head)
    print(head)