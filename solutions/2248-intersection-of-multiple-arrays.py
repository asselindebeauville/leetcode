"""2248. Intersection of Multiple Arrays

https://leetcode.com/problems/intersection-of-multiple-arrays/

>>> solution = Solution()
>>> solution.intersection([[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]])
[3, 4]
>>> solution.intersection([[1, 2, 3], [4, 5, 6]])
[]
"""


class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        result = set(nums[0])

        for i in range(1, len(nums)):
            result &= set(nums[i])

        return sorted(result)
