"""141. Linked List Cycle

https://leetcode.com/problems/linked-list-cycle/

>>> solution = Solution()
>>> # head = [3, 2, 0, -4], pos = 1
>>> n0, n1, n2, n3 = ListNode(3), ListNode(2), ListNode(0), ListNode(-4)
>>> n0.next, n1.next, n2.next, n3.next = n1, n2, n3, n1
>>> solution.hasCycle(n0)
True
>>> # head = [1, 2], pos = 0
>>> n0, n1 = ListNode(1), ListNode(2)
>>> n0.next, n1.next = n1, n0
>>> solution.hasCycle(n0)
True
>>> # head = [1], pos = -1
>>> n0 = ListNode(1)
>>> solution.hasCycle(n0)
False
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
