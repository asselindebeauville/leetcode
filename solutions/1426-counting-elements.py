"""1426. Counting Elements

https://leetcode.com/problems/counting-elements/

>>> solution = Solution()
>>> solution.countElements([1, 2, 3])
2
>>> solution.countElements([1, 1, 3, 3, 5, 5, 7, 7])
0
"""


class Solution:
    def countElements(self, arr: list[int]) -> int:
        num_set = set(arr)
        count = 0

        for num in arr:
            if num + 1 in num_set:
                count += 1

        return count
