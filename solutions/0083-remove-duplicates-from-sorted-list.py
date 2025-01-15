"""83. Remove Duplicates from Sorted List

https://leetcode.com/problems/remove-duplicates-from-sorted-list/

>>> solution = Solution()
>>> solution.deleteDuplicates([1, 1, 2])  # doctest: +SKIP
[1, 2]
>>> solution.deleteDuplicates([1, 1, 2, 3, 3])  # doctest: +SKIP
[1, 2, 3]
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head
