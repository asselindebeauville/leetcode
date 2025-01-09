"""1207. Unique Number of Occurrences

https://leetcode.com/problems/unique-number-of-occurrences/

>>> solution = Solution()
>>> solution.uniqueOccurrences([1, 2, 2, 1, 1, 3])
True
>>> solution.uniqueOccurrences([1, 2])
False
>>> solution.uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0])
True
"""

from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        counts = Counter(arr).values()
        seen = set()

        for count in counts:
            if count in seen:
                return False
            seen.add(count)

        return True
