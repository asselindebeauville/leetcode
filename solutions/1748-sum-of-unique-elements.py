"""1748. Sum of Unique Elements

https://leetcode.com/problems/sum-of-unique-elements/

>>> solution = Solution()
>>> solution.sumOfUnique([1, 2, 3, 2])
4
>>> solution.sumOfUnique([1, 1, 1, 1, 1])
0
>>> solution.sumOfUnique([1, 2, 3, 4, 5])
15
"""

from collections import Counter


class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        return sum(num for num, count in Counter(nums).items() if count == 1)
