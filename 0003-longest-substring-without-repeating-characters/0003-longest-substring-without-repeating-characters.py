class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lookup = set()
        left = 0
        max_leng = 0
        for right in range(len(s)):
            while s[right] in lookup:
                lookup.remove(s[left])
                left += 1
            lookup.add(s[right])
            max_leng = max(max_leng,right-left+1)
        return max_leng