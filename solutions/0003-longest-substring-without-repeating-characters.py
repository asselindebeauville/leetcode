"""3. Longest Substring Without Repeating Characters

https://leetcode.com/problems/longest-substring-without-repeating-characters/

>>> solution = Solution()
>>> solution.lengthOfLongestSubstring("abcabcbb")
3
>>> solution.lengthOfLongestSubstring("bbbbb")
1
>>> solution.lengthOfLongestSubstring("pwwkew")
3
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = max_length = 0
        char_pos = {}

        for right, char in enumerate(s):
            if char in char_pos:
                left = max(left, char_pos[char] + 1)

            max_length = max(max_length, right - left + 1)
            char_pos[char] = right

        return max_length
