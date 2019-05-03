# -*- coding: utf-8 -*-
# @Time    : 2019/3/11 0011 18:59
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0021_mergeTwoLists.py
# @Software: PyCharm

'''
21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        if l1 == None:
            return l2
        elif l2 == None:
            return l1

        if l1.val <= l2.val:
            mergepHead = l1
            mergepHead.next = self.mergeTwoLists(l1.next, l2)
        else:
            mergepHead = l2
            mergepHead.next = self.mergeTwoLists(l1, l2.next)
        return mergepHead

    def mergeTwoLists_1(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        else:

            if l1.val < l2.val:
                newlist = l1
                l1 = l1.next
            else:
                newlist = l2
                l2 = l2.next
            h = newlist
            while l1 and l2:
                if l1.val <= l2.val:
                    h.next = l1
                    h = h.next
                    l1 = l1.next
                else:
                    h.next = l2
                    h = h.next
                    l2 = l2.next

            while l1:
                h.next = l1
                l1 = l1.next
                h = h.next
            while l2:
                h.next = l2
                l2 = l2.next
                h = h.next
        return newlist

if __name__ == "__main__":
    '''
    list1: 1 -> 2 -> 4  list2: 1 -> 3 -> 4
    '''
    t1 = ListNode(1)
    t2 = ListNode(2)
    t3 = ListNode(4)
    t1.next = t2
    t2.next = t3
    l1 = t1

    t4 = ListNode(1)
    t5 = ListNode(3)
    t6 = ListNode(4)
    t4.next = t5
    t5.next = t6
    l2 = t4

    a = Solution()
    res = a.mergeTwoLists(l1, l2)
    print(res.val)

    t1 = ListNode(1)
    t2 = ListNode(2)
    t3 = ListNode(4)
    t1.next = t2
    t2.next = t3
    l1 = t1

    t4 = ListNode(1)
    t5 = ListNode(3)
    t6 = ListNode(4)
    t4.next = t5
    t5.next = t6
    l2 = t4

    a = Solution()
    res = a.mergeTwoLists_1(l1, l2)
    print(res.val)

