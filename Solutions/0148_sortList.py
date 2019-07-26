# -*- coding: utf-8 -*-
# @Time    : 2019/7/26 12:12
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0148_sortList.py
# @Software: PyCharm

'''
148. Sort List

Sort a linked list in O(n log n) time using constant space complexity.

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
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # merge sort, recursively
        if not head or not head.next:
            return head
        # divide list into two parts
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        # cut down the first part
        slow.next = None
        l = self.sortList(head)
        r = self.sortList(second)
        return self.merge(l, r)

    def merge(self, l, r):
        """
        :type l: ListNode
        :type r: ListNode
        :rtype: ListNode
        """
        # merge in-place without dummy node
        if not l or not r:
            return l or r
        if l.val > r.val:
            l, r = r, l
        # get the return node "head"
        head = pre = l
        l = l.next
        while l and r:
            if l.val < r.val:
                l = l.next
            else:
                nxt = pre.next
                pre.next = r
                tmp = r.next
                r.next = nxt
                r = tmp
            pre = pre.next
        # l and r at least one is None
        pre.next = l or r
        return head

    def sortList_1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        pre = head
        nums = []
        while pre:
            nums.append(pre.val)
            pre = pre.next
        nums.sort()
        pre = head
        for i in range(len(nums)):
            pre.val = nums[i]
            pre = pre.next

        return head

    def sortList_2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # merge sort, recursively
        if not head or not head.next:
            return head
        # divide list into two parts
        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None
        h1 = self.sortList_2(head)
        h2 = self.sortList_2(slow)
        return self.merge_1(h1, h2)

    def merge_1(self, h1, h2):
        """
        :type h1: ListNode
        :type h2: ListNode
        :rtype: ListNode
        """
        dummy = tail = ListNode(0)
        while h1 and h2:
            if h1.val < h2.val:
                tail.next, tail, h1 = h1, h1, h1.next
            else:
                tail.next, tail, h2 = h2, h2, h2.next

        tail.next = h1 or h2
        return dummy.next

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
    head = a.sortList(head)
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
    head = a.sortList_1(head)
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
    head = a.sortList_2(head)
    res = []
    while head:
        res += [head.val]
        head = head.next
    print(res)