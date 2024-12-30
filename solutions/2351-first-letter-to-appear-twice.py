"""2351. First Letter to Appear Twice

https://leetcode.com/problems/first-letter-to-appear-twice/

>>> solution = Solution()
>>> solution.repeatedCharacter("abccbaacz")
'c'
>>> solution.repeatedCharacter("abcdd")
'd'
"""


class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = set()

        for char in s:
            if char in seen:
                return char
            seen.add(char)
