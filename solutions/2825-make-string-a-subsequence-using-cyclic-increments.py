"""2825. Make String a Subsequence Using Cyclic Increments

https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/

>>> solution = Solution()
>>> solution.canMakeSubsequence("abc", "ad")
True
>>> solution.canMakeSubsequence("zc", "ad")
True
>>> solution.canMakeSubsequence("ab", "d")
False
"""


class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i, j = 0, 0

        while i < len(str1) and j < len(str2):
            diff = (ord(str2[j]) - ord(str1[i])) % 26
            if diff <= 1:
                j += 1
            i += 1

        return j == len(str2)
