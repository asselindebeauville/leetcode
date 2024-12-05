"""2109. Adding Spaces to a String

https://leetcode.com/problems/adding-spaces-to-a-string/

>>> solution = Solution()
>>> solution.addSpaces("LeetcodeHelpsMeLearn", [8, 13, 15])
'Leetcode Helps Me Learn'
>>> solution.addSpaces("icodeinpython", [1, 5, 7, 9])
'i code in py thon'
>>> solution.addSpaces("spacing", [0, 1, 2, 3, 4, 5, 6])
' s p a c i n g'
"""


class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        segments = []
        start = 0

        for end in spaces:
            segments.append(s[start:end])
            start = end
        segments.append(s[start:])

        return " ".join(segments)
