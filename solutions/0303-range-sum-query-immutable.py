"""303. Range Sum Query - Immutable

https://leetcode.com/problems/range-sum-query-immutable/

>>> obj = NumArray([-2, 0, 3, -5, 2, -1])
>>> obj.sumRange(0, 2)
1
>>> obj.sumRange(2, 5)
-1
>>> obj.sumRange(0, 5)
-3
"""

from itertools import accumulate


class NumArray:
    def __init__(self, nums: list[int]):
        self.prefix_sum = [0] + list(accumulate(nums))

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right + 1] - self.prefix_sum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
