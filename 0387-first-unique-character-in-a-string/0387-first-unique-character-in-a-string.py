from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        check = defaultdict(int)
        for i in range(len(s)):
            check[s[i]] += 1
        for i,char in enumerate(s):
            if check[char] == 1:
                return i
        return -1
        