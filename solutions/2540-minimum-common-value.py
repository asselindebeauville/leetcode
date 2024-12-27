"""2540. Minimum Common Value

https://leetcode.com/problems/minimum-common-value/

>>> solution = Solution()
>>> solution.getCommon([1, 2, 3], [2, 4])
2
>>> solution.getCommon([1, 2, 3, 6], [2, 3, 4, 5])
2
"""


class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        i = j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return -1
