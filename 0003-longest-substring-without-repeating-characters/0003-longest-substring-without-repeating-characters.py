class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        lookup = set()
        left = 0
        max_leng = 0
        for right in range(len(s)):
            if s[right] not in lookup:
                lookup.add(s[right])
                if right == len(s)-1:
                    max_leng = max(max_leng,right-left+1)
            else:
                max_leng = max(max_leng,right-left)
                while s[left] != s[right]:
                    print(left,right,s[left],lookup)
                    lookup.remove(s[left])
                    left += 1
                left += 1
        return max_leng