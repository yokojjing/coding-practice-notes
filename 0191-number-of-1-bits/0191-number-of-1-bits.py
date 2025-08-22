class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1  # Check if rightmost bit is 1
            n >>= 1        # Right shift by 1 (equivalent to n //= 2)
        return count