"""917. Reverse Only Letters

https://leetcode.com/problems/reverse-only-letters/

>>> solution = Solution()
>>> solution.reverseOnlyLetters("ab-cd")
'dc-ba'
>>> solution.reverseOnlyLetters("a-bC-dEf-ghIj")
'j-Ih-gfE-dCba'
>>> solution.reverseOnlyLetters("Test1ng-Leet=code-Q!")
'Qedo1ct-eeLg=ntse-T!'
"""


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        chars = list(s)
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not chars[left].isalpha():
                left += 1
            while left < right and not chars[right].isalpha():
                right -= 1

            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1

        return "".join(chars)
