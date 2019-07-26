# -*- coding: utf-8 -*-
# @Time    : 2019/7/26 7:46
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0147_insertionSortList.py
# @Software: PyCharm

'''
147. Insertion Sort List

Sort a linked list using insertion sort.

A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list

Algorithm of Insertion Sort:
Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data,
finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

Example 1:
Input: 4->2->1->3
Output: 1->2->3->4

Example 2:
Input: -1->5->3->4->0
Output: -1->0->3->4->5
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = node = head
        while node.next:
            if node.val <= node.next.val:
                node = node.next
            else:
                pre = dummy
                while pre.next.val < node.next.val:
                    pre = pre.next
                tmp = node.next
                node.next = tmp.next
                tmp.next = pre.next
                pre.next = tmp
        return dummy.next

    def insertionSortList_1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # brutal solution
        res = []
        dummy1 = dummy2 = ListNode(0)
        size = 0
        while head:
            size += 1
            res += [head.val]
            head = head.next

        res.sort()
        for i in range(size):
            dummy1.next = ListNode(res[i])
            dummy1 = dummy1.next
        return dummy2.next

if __name__ == "__main__":
    a = Solution()

    '''
     4 -> 2 -> 1 -> 3

    '''
    l1 = ListNode(4)
    l2 = ListNode(2)
    l3 = ListNode(1)
    l4 = ListNode(3)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    head = l1
    head = a.insertionSortList(head)
    res = []
    while head:
        res += [head.val]
        head = head.next
    print(res)

    l1 = ListNode(4)
    l2 = ListNode(2)
    l3 = ListNode(1)
    l4 = ListNode(3)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    head = l1
    head = a.insertionSortList_1(head)
    res = []
    while head:
        res += [head.val]
        head = head.next
    print(res)

    '''
     -1 -> 5 -> 3 -> 4 -> 0

    '''
    l1 = ListNode(-1)
    l2 = ListNode(5)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(0)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    head = l1
    head = a.insertionSortList(head)
    res = []
    while head:
        res += [head.val]
        head = head.next
    print(res)

    l1 = ListNode(-1)
    l2 = ListNode(5)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(0)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    head = l1
    head = a.insertionSortList_1(head)
    res = []
    while head:
        res += [head.val]
        head = head.next
    print(res)