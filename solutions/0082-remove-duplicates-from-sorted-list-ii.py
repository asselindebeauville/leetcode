"""82. Remove Duplicates from Sorted List II

https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

>>> solution = Solution()
>>> solution.deleteDuplicates([1, 2, 3, 3, 4, 4, 5])  # doctest: +SKIP
[1, 2, 5]
>>> solution.deleteDuplicates([1, 1, 1, 2, 3])  # doctest: +SKIP
[2, 3]
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = dummy = ListNode(0, head)
        current = head

        while current:
            if current.next and current.val == current.next.val:
                while current.next and current.val == current.next.val:
                    current = current.next

                prev.next = current.next
            else:
                prev = current

            current = current.next

        return dummy.next
