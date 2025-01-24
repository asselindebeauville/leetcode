"""346. Moving Average from Data Stream

https://leetcode.com/problems/moving-average-from-data-stream/

>>> obj = MovingAverage(3)
>>> obj.next(1)
1.0
>>> obj.next(10)
5.5
>>> obj.next(3)
4.666666666666667
>>> obj.next(5)
6.0
"""

from collections import deque


class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.window = deque()
        self.window_sum = 0

    def next(self, val: int) -> float:
        self.window.append(val)
        self.window_sum += val

        if len(self.window) > self.size:
            self.window_sum -= self.window.popleft()

        return self.window_sum / len(self.window)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
