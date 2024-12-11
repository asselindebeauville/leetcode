"""383. Ransom Note

https://leetcode.com/problems/ransom-note/

>>> solution = Solution()
>>> solution.canConstruct("a", "b")
False
>>> solution.canConstruct("aa", "ab")
False
>>> solution.canConstruct("aa", "aab")
True
"""

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        counts = Counter(magazine)

        for char in ransomNote:
            if not counts[char]:
                return False
            counts[char] -= 1

        return True
