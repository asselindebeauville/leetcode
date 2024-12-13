"""167. Two Sum II - Input Array Is Sorted

https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

>>> solution = Solution()
>>> solution.twoSum([2, 7, 11, 15], 9)
[1, 2]
>>> solution.twoSum([2, 3, 4], 6)
[1, 3]
>>> solution.twoSum([-1, 0], -1)
[1, 2]
"""


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]

            if total == target:
                return [left + 1, right + 1]
            elif total < target:
                left += 1
            else:
                right -= 1
