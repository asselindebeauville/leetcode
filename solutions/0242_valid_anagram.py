"""242. Valid Anagram

https://leetcode.com/problems/valid-anagram/

>>> solution = Solution()
>>> solution.isAnagram("anagram", "nagaram")
True
>>> solution.isAnagram("rat", "car")
False
"""

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return Counter(s) == Counter(t)
