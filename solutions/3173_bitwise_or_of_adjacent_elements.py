"""3173. Bitwise OR of Adjacent Elements

https://leetcode.com/problems/bitwise-or-of-adjacent-elements/

>>> solution = Solution()
>>> solution.orArray([1, 3, 7, 15])
[3, 7, 15]
>>> solution.orArray([8, 4, 2])
[12, 6]
>>> solution.orArray([5, 4, 9, 11])
[5, 13, 11]
"""


class Solution:
    def orArray(self, nums: list[int]) -> list[int]:
        return [nums[i] | nums[i + 1] for i in range(len(nums) - 1)]
