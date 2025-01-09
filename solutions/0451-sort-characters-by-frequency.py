"""451. Sort Characters By Frequency

https://leetcode.com/problems/sort-characters-by-frequency/

>>> solution = Solution()
>>> solution.frequencySort("tree")  # doctest: +SKIP
'eert'
>>> solution.frequencySort("cccaaa")  # doctest: +SKIP
'aaaccc'
>>> solution.frequencySort("Aabb")  # doctest: +SKIP
'bbAa'
"""

from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        string_builder = []

        for char, count in counts.most_common():
            string_builder.append(char * count)

        return "".join(string_builder)
