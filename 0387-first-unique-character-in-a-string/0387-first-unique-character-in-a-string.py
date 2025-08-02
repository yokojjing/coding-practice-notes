class Solution:
    from collections import defaultdict
    def firstUniqChar(self, s: str) -> int:
        check = defaultdict(int)
        for i in range(len(s)):
            check[s[i]] += 1
        for i in check:
            if check[i] == 1:
                return s.index(i)
        return -1
        