"""1941. Check if All Characters Have Equal Number of Occurrences

https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/

>>> solution = Solution()
>>> solution.areOccurrencesEqual("abacbc")
True
>>> solution.areOccurrencesEqual("aaabb")
False
"""

from collections import Counter


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        return len(set(Counter(s).values())) == 1
