"""977. Squares of a Sorted Array

https://leetcode.com/problems/squares-of-a-sorted-array/

>>> solution = Solution()
>>> solution.sortedSquares([-4, -1, 0, 3, 10])
[0, 1, 9, 16, 100]
>>> solution.sortedSquares([-7, -3, 2, 3, 11])
[4, 9, 9, 49, 121]
"""


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        squares = [0] * n
        left, right = 0, n - 1

        for i in reversed(range(n)):
            if abs(nums[left]) > abs(nums[right]):
                squares[i] = nums[left] ** 2
                left += 1
            else:
                squares[i] = nums[right] ** 2
                right -= 1

        return squares
