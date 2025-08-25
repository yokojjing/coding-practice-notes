class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(left,right):
            count = 0
            while left>=0 and right<=len(s)-1 and s[left]==s[right]:
                left -= 1
                right += 1
                count += 1
            return count
        result = 0
        for i in range(0,len(s)):
            result += expand(i,i)
            result += expand(i,i+1)
        return result