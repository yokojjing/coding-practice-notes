class Solution:
    def romanToInt(self, s: str) -> int:
        value = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        total = 0
        for i in range(len(s)):
            if i < len(s)-1 and value[s[i]] < value[s[i+1]]:
                total -= value[s[i]]
            else:
                total += value[s[i]]
        return total
