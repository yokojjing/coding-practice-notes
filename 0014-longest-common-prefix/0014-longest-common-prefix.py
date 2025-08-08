class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_leng = min(len(s) for s in strs)
        i = 0
        for i in range(min_leng):
            char = strs[0][i]
            for j in range(1,len(strs)):
                if char != strs[j][i]:
                    return strs[0][:i]
        return strs[0][:min_leng]
            