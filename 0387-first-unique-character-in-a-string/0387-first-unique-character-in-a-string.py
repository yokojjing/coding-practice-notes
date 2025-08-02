from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        check = Counter(s)
        for i in check:
            if check[i] == 1:
                return s.index(i)
        return -1
        