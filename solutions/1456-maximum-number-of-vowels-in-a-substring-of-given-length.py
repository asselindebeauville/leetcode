"""1456. Maximum Number of Vowels in a Substring of Given Length

https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

>>> solution = Solution()
>>> solution.maxVowels("abciiidef", 3)
3
>>> solution.maxVowels("aeiou", 2)
2
>>> solution.maxVowels("leetcode", 3)
2
"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        count = 0

        for i in range(k):
            count += s[i] in vowels

        max_vowels = count
        for i in range(k, len(s)):
            count += (s[i] in vowels) - (s[i - k] in vowels)
            max_vowels = max(max_vowels, count)

        return max_vowels
