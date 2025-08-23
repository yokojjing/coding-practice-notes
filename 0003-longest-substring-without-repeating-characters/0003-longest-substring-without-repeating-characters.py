class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        max_leng = 0
        left = 0
        for right in range(len(s)):
            if s[right] in char_index and char_index[s[right]] >= left:
                left = char_index[s[right]] +1
            char_index[s[right]] = right
            max_leng = max(max_leng,right-left+1)
        return max_leng