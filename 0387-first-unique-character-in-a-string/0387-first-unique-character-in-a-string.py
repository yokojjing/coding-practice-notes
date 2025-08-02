from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        check = Counter(s)
        for i,v in enumerate(s):
            if check[v] == 1:
                return i
        return -1
        