from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        check = defaultdict(int)
        longest = 0
        maxfreq = 0
        for i in range(len(s)):
            check[s[i]] += 1
            maxfreq = max(check[s[i]],maxfreq)
            if (i-left+1) - maxfreq > k:
                check[s[left]] -= 1
                left += 1
            
            longest = max(longest,i-left+1)
        
        return longest