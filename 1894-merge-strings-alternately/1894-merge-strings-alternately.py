class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1) > len(word2):
            long,short = word1,word2
        else:
            long,short = word2,word1
        i = 0
        result = ''
        while i < len(short):
            result += word1[i] + word2[i]
            i += 1
        result += long[i:]
        return result