from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        check = defaultdict(list)
        for i in range(len(s)):
            check[s[i]].append(i)
        for i in check:
            if len(check[i]) == 1:
                return check[i][0]
        return -1
        