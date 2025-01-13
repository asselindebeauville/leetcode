"""1657. Determine if Two Strings Are Close

https://leetcode.com/problems/determine-if-two-strings-are-close/

>>> solution = Solution()
>>> solution.closeStrings("abc", "bca")
True
>>> solution.closeStrings("a", "aa")
False
>>> solution.closeStrings("cabbba", "abbccc")
True
"""

from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        if set(word1) != set(word2):
            return False

        return sorted(Counter(word1).values()) == sorted(Counter(word2).values())
