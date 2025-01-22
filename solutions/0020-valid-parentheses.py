"""20. Valid Parentheses

https://leetcode.com/problems/valid-parentheses/

>>> solution = Solution()
>>> solution.isValid("()")
True
>>> solution.isValid("()[]{}")
True
>>> solution.isValid("(]")
False
>>> solution.isValid("([])")
True
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {"(": ")", "{": "}", "[": "]"}

        for char in s:
            if char in bracket_map:
                stack.append(bracket_map[char])
            else:
                if not stack or stack.pop() != char:
                    return False

        return not stack
