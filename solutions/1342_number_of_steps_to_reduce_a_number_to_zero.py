"""1342. Number of Steps to Reduce a Number to Zero

https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

>>> solution = Solution()
>>> solution.numberOfSteps(14)
6
>>> solution.numberOfSteps(8)
4
>>> solution.numberOfSteps(123)
12
"""


class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0

        return num.bit_length() - 1 + num.bit_count()
