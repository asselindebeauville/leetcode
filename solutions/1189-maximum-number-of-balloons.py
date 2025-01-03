"""1189. Maximum Number of Balloons

https://leetcode.com/problems/maximum-number-of-balloons/

>>> solution = Solution()
>>> solution.maxNumberOfBalloons("nlaebolko")
1
>>> solution.maxNumberOfBalloons("loonbalxballpoon")
2
>>> solution.maxNumberOfBalloons("leetcode")
0
"""

from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        char_count = Counter(text)
        balloon_count = Counter("balloon")

        return min(char_count[char] // balloon_count[char] for char in balloon_count)
