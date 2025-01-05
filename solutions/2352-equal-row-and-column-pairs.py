"""2352. Equal Row and Column Pairs

https://leetcode.com/problems/equal-row-and-column-pairs/

>>> solution = Solution()
>>> solution.equalPairs([[3, 2, 1], [1, 7, 6], [2, 7, 7]])
1
>>> solution.equalPairs([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]])
3
"""

from collections import Counter


class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        row_count = Counter(map(tuple, grid))
        return sum(row_count[col_tuple] for col_tuple in zip(*grid))
