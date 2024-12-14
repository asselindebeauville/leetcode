"""392. Is Subsequence

https://leetcode.com/problems/is-subsequence/

>>> solution = Solution()
>>> solution.isSubsequence("abc", "ahbgdc")
True
>>> solution.isSubsequence("axc", "ahbgdc")
False
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)
