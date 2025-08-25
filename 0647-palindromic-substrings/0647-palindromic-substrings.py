class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(left,right):
            while left>=0 and right<=len(s)-1 and s[left]==s[right]:
                left -= 1
                right += 1
            return (right-left)//2
        sub_sum = 0
        for i in range(0,len(s)-1):
            sub_sum += expand(i,i)
            sub_sum += expand(i,i+1)
        return sub_sum+1