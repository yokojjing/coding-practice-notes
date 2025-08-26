class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        match_to = [False]*(n+1)
        match_to[0] = True
        for i in range(1,n+1):
            for j in range(i):
                if match_to[j] and s[j:i] in word_set:
                    match_to[i] = True
                    break
        return match_to[n]
                