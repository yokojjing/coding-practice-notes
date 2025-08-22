class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1,n+1):
            output = ''
            if i%3 == 0:
                output += 'Fizz'
            if i%5 == 0:
                output += 'Buzz'
            result.append(output or str(i))
        return result
            