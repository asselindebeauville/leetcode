"""496. Next Greater Element I

https://leetcode.com/problems/next-greater-element-i/

>>> solution = Solution()
>>> solution.nextGreaterElement([4, 1, 2], [1, 3, 4, 2])
[-1, 3, -1]
>>> solution.nextGreaterElement([2, 4], [1, 2, 3, 4])
[3, -1]
"""


class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        next_greater = {}
        stack = []

        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)

        return [next_greater.get(num, -1) for num in nums1]
