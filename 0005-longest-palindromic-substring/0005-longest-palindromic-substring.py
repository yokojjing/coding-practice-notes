class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        start = 0
        max_leng = 1
        def expand(left:int,right:int):
            while left >= 0 and right <= len(s)-1 and s[left] == s[right]:
                left -= 1
                right += 1
            return right-left-1
        for i in range(len(s)-1):
            max1 = expand(i,i)
            max2 = expand(i,i+1)
            current = max(max1,max2)
            if current > max_leng:
                max_leng = current
                start = i-(max_leng-1)//2
        return s[start:start+max_leng]