"""92. Reverse Linked List II

https://leetcode.com/problems/reverse-linked-list-ii/

>>> solution = Solution()
>>> solution.reverseBetween([1, 2, 3, 4, 5], 2, 4)  # doctest: +SKIP
[1, 4, 3, 2, 5]
>>> solution.reverseBetween([5], 1, 1)  # doctest: +SKIP
[5]
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if not head or left == right:
            return head

        prev = dummy = ListNode(0, head)

        for _ in range(left - 1):
            prev = prev.next

        current = prev.next

        for _ in range(right - left):
            next_node = current.next
            current.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node

        return dummy.next
