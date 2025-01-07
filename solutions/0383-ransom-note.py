"""383. Ransom Note

https://leetcode.com/problems/ransom-note/

>>> solution = Solution()
>>> solution.canConstruct("a", "b")
False
>>> solution.canConstruct("aa", "ab")
False
>>> solution.canConstruct("aa", "aab")
True
>>> solution.canConstruct("aa", "a")
False
"""

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        return not Counter(ransomNote) - Counter(magazine)
