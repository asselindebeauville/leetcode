"""791. Custom Sort String

https://leetcode.com/problems/custom-sort-string/

>>> solution = Solution()
>>> solution.customSortString("cba", "abcd")
'cbad'
>>> solution.customSortString("bcafg", "abcd")
'bcad'
"""

from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counts = Counter(s)
        chars = []

        for char in order:
            chars.extend([char] * counts[char])
            del counts[char]

        for char, count in counts.items():
            chars.extend([char] * count)

        return "".join(chars)
