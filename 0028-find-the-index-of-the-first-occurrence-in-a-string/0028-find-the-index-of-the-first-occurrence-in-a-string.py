class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def lps(pattern):
            lps = [0] * len(pattern)
            leng = 0
            i = 1
            while i < len(pattern):
                if pattern[i] == pattern[leng]:
                    leng += 1
                    lps[i] = leng
                    i += 1
                else:
                    if leng != 0:
                        leng = lps[leng-1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps

        needle_lps = lps(needle)
        i = 0
        j = 0
        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == len(needle):
                    return i-j
            elif j != 0:
                j = needle_lps[j-1]
            else:
                i += 1
        return -1
        

        