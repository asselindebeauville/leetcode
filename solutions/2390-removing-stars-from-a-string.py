"""2390. Removing Stars From a String

https://leetcode.com/problems/removing-stars-from-a-string/

>>> solution = Solution()
>>> solution.removeStars("leet**cod*e")
'lecoe'
>>> solution.removeStars("erase*****")
''
"""


class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for char in s:
            if char == "*":
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack)
