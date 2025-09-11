class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        lookup = {}
        def startmatch(str_idx,pat_idx):
            if (str_idx,pat_idx) in lookup:
                return lookup[(str_idx,pat_idx)]
            if pat_idx == len(t):
                lookup[(str_idx,pat_idx)] = 1
                return 1
            if str_idx == len(s):
                lookup[(str_idx,pat_idx)] = 0
                return 0
            a = 0
            if s[str_idx] == t[pat_idx]:
                a = startmatch(str_idx+1,pat_idx+1)
            b = startmatch(str_idx+1,pat_idx)
            lookup[(str_idx,pat_idx)] = a+b
            return lookup[(str_idx,pat_idx)]
        return startmatch(0,0)
