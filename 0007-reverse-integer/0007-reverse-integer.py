class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x *= sign
        target = 0
        while x != 0:
            digits = x%10
            target = target*10 + digits
            x //= 10
        target *= sign
        return target if (-(2**31) <= target <= 2**31 -1) else 0