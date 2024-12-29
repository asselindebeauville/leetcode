"""1208. Get Equal Substrings Within Budget

https://leetcode.com/problems/get-equal-substrings-within-budget/

>>> solution = Solution()
>>> solution.equalSubstring("abcd", "bcdf", 3)
3
>>> solution.equalSubstring("abcd", "cdef", 3)
1
>>> solution.equalSubstring("abcd", "acde", 0)
1
"""


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = curr_cost = max_length = 0

        for right in range(len(s)):
            curr_cost += abs(ord(s[right]) - ord(t[right]))

            while curr_cost > maxCost:
                curr_cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
