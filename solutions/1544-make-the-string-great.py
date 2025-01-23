"""1544. Make The String Great

https://leetcode.com/problems/make-the-string-great/

>>> solution = Solution()
>>> solution.makeGood("leEeetcode")
'leetcode'
>>> solution.makeGood("abBAcC")
''
>>> solution.makeGood("s")
's'
"""


class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for char in s:
            if stack and (char.lower() == stack[-1].lower() and char != stack[-1]):
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack)
