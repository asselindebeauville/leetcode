"""347. Top K Frequent Elements

https://leetcode.com/problems/top-k-frequent-elements/

>>> solution = Solution()
>>> result = solution.topKFrequent([1, 1, 1, 2, 2, 3], 2)
>>> sorted(result)
[1, 2]
>>> solution.topKFrequent([1], 1)
[1]
"""

from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        return [num[0] for num in Counter(nums).most_common(k)]
