"""283. Move Zeroes

https://leetcode.com/problems/move-zeroes/

>>> solution = Solution()
>>> nums = [0, 1, 0, 3, 12]
>>> solution.moveZeroes(nums)
>>> nums
[1, 3, 12, 0, 0]
>>> nums = [0]
>>> solution.moveZeroes(nums)
>>> nums
[0]
"""


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0

        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
