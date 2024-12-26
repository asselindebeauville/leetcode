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
        rules = {3: "Fizz", 5: "Buzz"}
        answer = []

        for i in range(1, n + 1):
            string_builder = []

            for divisor, word in rules.items():
                if i % divisor == 0:
                    string_builder.append(word)

            answer.append("".join(string_builder) if string_builder else str(i))

        return answer
