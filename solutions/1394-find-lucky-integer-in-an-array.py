"""1394. Find Lucky Integer in an Array

https://leetcode.com/problems/find-lucky-integer-in-an-array/

>>> solution = Solution()
>>> solution.findLucky([2, 2, 3, 4])
2
>>> solution.findLucky([1, 2, 2, 3, 3, 3])
3
>>> solution.findLucky([2, 2, 2, 3, 3])
-1
"""

from collections import Counter


class Solution:
    def findLucky(self, arr: list[int]) -> int:
        return max(
            (num for num, count in Counter(arr).items() if num == count),
            default=-1,
        )
