class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        sign = 1
        left = 0
        
        while left < len(s) and s[left] == ' ':
            left += 1
        
        if left >= len(s):
            return 0
        
        if s[left] == '-' or s[left] == '+':
            if s[left] == '-':
                sign = -1 
            left += 1
        
        right = left
        while right < len(s) and s[right].isdigit():
            right += 1
        
        number = s[left:right]
        
        if len(number) == 0:
            return 0
        
        result = sign*int(number)
        
        if result < -2**31:
            return -2**31
        if result > 2**31-1:
            return 2**31-1
        return result
        
        
        