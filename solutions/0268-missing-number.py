"""268. Missing Number

https://leetcode.com/problems/missing-number/

>>> solution = Solution()
>>> solution.missingNumber([3, 0, 1])
2
>>> solution.missingNumber([0, 1])
2
>>> solution.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1])
8
"""


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        expected_sum = (n * (n + 1)) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
