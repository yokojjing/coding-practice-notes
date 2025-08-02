from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        check = defaultdict(int)
        for i in range(len(s)):
            check[s[i]] += 1
            check[t[i]] -= 1
        for i,v in check.items():
            if v != 0:
                return False
        return True