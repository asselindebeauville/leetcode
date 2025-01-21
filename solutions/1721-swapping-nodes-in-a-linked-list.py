"""1721. Swapping Nodes in a Linked List

https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

>>> solution = Solution()  # doctest: +SKIP
>>> solution.swapNodes([1, 2, 3, 4, 5], 2)  # doctest: +SKIP
[1, 4, 3, 2, 5]
>>> solution.swapNodes([7, 9, 6, 6, 7, 8, 3, 0, 9, 5], 5)  # doctest: +SKIP
[7, 9, 6, 6, 8, 7, 3, 0, 9, 5]
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow = fast = head

        for _ in range(k - 1):
            fast = fast.next
        first = fast

        while fast.next:
            slow = slow.next
            fast = fast.next
        second = slow

        first.val, second.val = second.val, first.val

        return head
