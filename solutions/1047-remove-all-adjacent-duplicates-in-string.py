"""1047. Remove All Adjacent Duplicates In String

https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

>>> solution = Solution()
>>> solution.removeDuplicates("abbaca")
'ca'
>>> solution.removeDuplicates("azxxzy")
'ay'
"""


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack)
