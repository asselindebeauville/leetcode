"""3005. Count Elements With Maximum Frequency

https://leetcode.com/problems/count-elements-with-maximum-frequency/

>>> solution = Solution()
>>> solution.maxFrequencyElements([1, 2, 2, 3, 1, 4])
4
>>> solution.maxFrequencyElements([1, 2, 3, 4, 5])
5
"""

from collections import Counter


class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        freqs = Counter(nums).values()
        max_freq = max(freqs)
        return sum(freq for freq in freqs if freq == max_freq)
