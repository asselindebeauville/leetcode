"""1346. Check If N and Its Double Exist

https://leetcode.com/problems/check-if-n-and-its-double-exist/

>>> solution = Solution()
>>> solution.checkIfExist([10, 2, 5, 3])
True
>>> solution.checkIfExist([3, 1, 7, 11])
False
"""


class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        seen = set()

        for num in arr:
            if num * 2 in seen or num / 2 in seen:
                return True
            seen.add(num)

        return False
