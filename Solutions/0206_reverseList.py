# -*- coding: utf-8 -*-
# @Time    : 2019/9/1 9:58
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0206_reverseList.py
# @Software: PyCharm

'''
206. Reverse Linked List

Reverse a singly linked list.

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:
A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # Iteratively
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        pre = None
        while head:
            tmp = head.next
            head.next = pre
            pre = head
            head = tmp
        return pre

    # Recursively
    def reverseList_1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.helper(head, None)

    def helper(self, head, pre):
        if not head:
            return pre
        tmp = head.next
        head.next = pre
        return self.helper(tmp, head)

if __name__ == "__main__":
    a = Solution()

    '''
     1 -> 2 -> 3 -> 4 -> 5

    '''
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    head = l1
    head = a.reverseList(head)
    res = []
    while head:
        res += [head.val]
        head = head.next
    print(res)

    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    head = l1
    head = a.reverseList_1(head)
    res = []
    while head:
        res += [head.val]
        head = head.next
    print(res)