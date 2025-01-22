"""234. Palindrome Linked List

https://leetcode.com/problems/palindrome-linked-list/

>>> solution = Solution()
>>> # head = [1, 2, 2, 1]
>>> solution.isPalindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(1)))))
True
>>> # head = [1, 2]
>>> solution.isPalindrome(ListNode(1, ListNode(2)))
False
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prev = None
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next

            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        if fast:
            slow = slow.next

        while slow:
            if slow.val != prev.val:
                return False
            prev = prev.next
            slow = slow.next

        return True
