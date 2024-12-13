"""2554. Maximum Number of Integers to Choose From a Range I

https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/

>>> solution = Solution()
>>> solution.maxCount([1, 6, 5], 5, 6)
2
>>> solution.maxCount([1, 2, 3, 4, 5, 6, 7], 8, 1)
0
>>> solution.maxCount([11], 7, 50)
7
"""


class Solution:
    def maxCount(self, banned: list[int], n: int, maxSum: int) -> int:
        banned_set = set(banned)
        total = 0
        count = 0

        for num in range(1, n + 1):
            if num in banned_set:
                continue

            total += num
            if total > maxSum:
                break
            count += 1

        return count
