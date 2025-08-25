class Solution:
    def countSubstrings(self, s: str) -> int:
        sub_sum = 0
        for i in range(1,len(s)+1):
            for j in range(0,len(s)-i+1):
                if s[j:j+i] == s[j:j+i][::-1]:
                    sub_sum += 1
        return sub_sum