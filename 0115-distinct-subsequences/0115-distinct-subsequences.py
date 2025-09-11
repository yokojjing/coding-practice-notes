class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        def dp(i,j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0

            if (i,j) in memo:
                return memo[(i,j)]
            if s[i] == t[j]:
                use = dp(i+1,j+1)
                skip = dp(i+1,j)
                result = use+skip
            else:
                result = dp(i+1,j)
            memo[(i,j)] = result
            return result
        return dp(0,0)
