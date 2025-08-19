class Solution:
    def climbStairs(self, n: int) -> int:
        prev1,prev2 = 1,1
        for i in range(2,n+1):
            current = prev1+prev2
            prev1,prev2 = prev2,current
        return prev2