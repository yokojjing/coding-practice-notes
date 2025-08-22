class Solution:
    def hammingWeight(self, n: int) -> int:
        current = n
        digit_sum = 0
        while current//2 != 0:
            digit_sum += current % 2
            current //= 2
        return digit_sum+1