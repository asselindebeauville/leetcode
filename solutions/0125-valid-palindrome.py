"""125. Valid Palindrome

https://leetcode.com/problems/valid-palindrome/

>>> solution = Solution()
>>> solution.isPalindrome("A man, a plan, a canal: Panama")
True
>>> solution.isPalindrome("race a car")
False
>>> solution.isPalindrome(" ")
True
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
