"""2095. Delete the Middle Node of a Linked List

https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

>>> solution = Solution()  # doctest: +SKIP
>>> solution.deleteMiddle([1, 3, 4, 7, 1, 2, 6])  # doctest: +SKIP
[1, 3, 4, 1, 2, 6]
>>> solution.deleteMiddle([1, 2, 3, 4])  # doctest: +SKIP
[1, 2, 4]
>>> solution.deleteMiddle([2, 1])  # doctest: +SKIP
[2]
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        slow = head
        fast = head.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next

        return head
