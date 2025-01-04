"""525. Contiguous Array

https://leetcode.com/problems/contiguous-array/

>>> solution = Solution()
>>> solution.findMaxLength([0, 1])
2
>>> solution.findMaxLength([0, 1, 0])
2
"""


class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        count = max_length = 0
        count_index_map = {0: -1}

        for i, num in enumerate(nums):
            count += 1 if num else -1

            if count in count_index_map:
                max_length = max(max_length, i - count_index_map[count])
            else:
                count_index_map[count] = i

        return max_length
