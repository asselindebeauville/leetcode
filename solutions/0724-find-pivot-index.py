"""724. Find Pivot Index

https://leetcode.com/problems/find-pivot-index/

>>> solution = Solution()
>>> solution.pivotIndex([1, 7, 3, 6, 5, 6])
3
>>> solution.pivotIndex([1, 2, 3])
-1
>>> solution.pivotIndex([2, 1, -1])
0
"""


class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left_sum, right_sum = 0, sum(nums)

        for i, num in enumerate(nums):
            right_sum -= num
            if left_sum == right_sum:
                return i
            left_sum += num

        return -1
