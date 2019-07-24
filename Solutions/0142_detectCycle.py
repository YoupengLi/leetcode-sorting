# -*- coding: utf-8 -*-
# @Time    : 2019/7/24 15:38
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0142_detectCycle.py
# @Software: PyCharm

'''
142. Linked List Cycle II

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed)
in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.


Example 1:
           ——————————
          |          |
          V          |
     3 -> 2 -> 0 -> -4
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
      ————
     |    |
     V    |
     1 -> 2
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
    1
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.

Follow-up:
Can you solve it without using extra space?

解题思路：首先使用快慢指针技巧，如果fast指针和slow指针相遇，则说明链表存在环路。
在fast指针和slow指针相遇后，fast指针不动，slow指针回到head，然后slow指针和fast指针同时向前走，只不过这一次两个指针都是一步一步向前走。
两个指针相遇的节点就是环路的起点。

原理说明：
head到环路起点的距离为K，起点到fast和slow的相遇点的距离为M，环路周长为L。假设在fast和slow相遇时，fast走过了Lfast，slow走过了Lslow。
根据题意：
Lslow=K+M；Lfast=K+M+n*L（n为正整数）；Lfast=2*Lslow
可以推出：Lslow=n*L；K=n*L-M
则当fast重新回到head，而slow还在相遇点，slow和fast都向前走，且每次走一个节点。
则fast从head走到起点走了K，而slow从相遇点出发也走了K，由于K=（n-1）*L+（L-M），所以slow转了n-1圈，再走L-M，也到了起点。
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            # if there is a cycle
            if slow is fast:
                # the head and slow nodes move step by step
                while head:
                    if head == slow:
                        return head
                    head = head.next
                    slow = slow.next
        return None

    def detectCycle_1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None

        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        # no cycle
        if not fast.next or not fast.next.next:
            return None

        fast = head
        while slow != fast:
            fast = fast.next
            slow = slow.next

        return slow

if __name__ == "__main__":
    a = Solution()

    '''
           ——————————
          |          |
          V          |
     3 -> 2 -> 0 -> -4

    '''
    l1 = ListNode(3)
    l2 = ListNode(2)
    l3 = ListNode(0)
    l4 = ListNode(-4)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l2
    head = l1
    print(a.detectCycle(head).val)
    print(a.detectCycle_1(head).val)

    '''
      ————
     |    |
     V    |
     1 -> 2

    '''
    l1 = ListNode(1)
    l2 = ListNode(2)
    l1.next = l2
    l2.next = l1
    head = l1
    print(a.detectCycle(head).val)
    print(a.detectCycle_1(head).val)

    '''
    1

    '''
    l1 = ListNode(1)
    head = l1
    print(a.detectCycle(head))
    print(a.detectCycle_1(head))