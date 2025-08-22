class Solution:
    def romanToInt(self, s: str) -> int:
        values = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        pre_value = 0
        total = 0
        for char in reversed(s):
            value = values[char]
            if value < pre_value:
                total -= value
            else:
                total += value
            pre_value = value
        return total
