class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            s
        max_leng = s[0]
        for i in range(0,len(s)-1):
            for j in range(i+1):
                left = j
                right = len(s)-1-i+j
                sign = True
                while left < right:
                    if s[left] != s[right]:
                        sign = False
                        break
                    left += 1
                    right -= 1
                if sign:
                    max_leng = s[j:len(s)-i+j]
                    return max_leng
        return max_leng