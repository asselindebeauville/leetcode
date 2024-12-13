"""412. Fizz Buzz

https://leetcode.com/problems/fizz-buzz/

>>> solution = Solution()
>>> solution.fizzBuzz(3)
['1', '2', 'Fizz']
>>> solution.fizzBuzz(5)
['1', '2', 'Fizz', '4', 'Buzz']
>>> solution.fizzBuzz(15)
['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
"""


class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        answer = []

        for i in range(1, n + 1):
            string = ""

            if i % 3 == 0:
                string += "Fizz"
            if i % 5 == 0:
                string += "Buzz"
            if not string:
                string = str(i)

            answer.append(string)

        return answer
