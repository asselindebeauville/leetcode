"""49. Group Anagrams

https://leetcode.com/problems/group-anagrams/

>>> solution = Solution()
>>> result = solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
>>> sorted([sorted(group) for group in result])
[['ate', 'eat', 'tea'], ['bat'], ['nat', 'tan']]
>>> solution.groupAnagrams([""])
[['']]
>>> solution.groupAnagrams(["a"])
[['a']]
"""

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)

        for string in strs:
            counts = [0] * 26
            for char in string:
                counts[ord(char) - ord("a")] += 1
            groups[tuple(counts)].append(string)

        return list(groups.values())
