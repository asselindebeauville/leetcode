"""344. Reverse String

https://leetcode.com/problems/reverse-string/

>>> solution = Solution()
>>> s = ["h", "e", "l", "l", "o"]
>>> solution.reverseString(s)
>>> s
['o', 'l', 'l', 'e', 'h']
>>> s = ["H", "a", "n", "n", "a", "h"]
>>> solution.reverseString(s)
>>> s
['h', 'a', 'n', 'n', 'a', 'H']
"""


class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
