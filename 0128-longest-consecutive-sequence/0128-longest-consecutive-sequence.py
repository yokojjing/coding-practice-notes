class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        lookup = set(nums)
        max_sum = 0
        for i in lookup:
            if i-1 not in lookup:
                num = i
                while num+1 in lookup:
                    num += 1
                max_sum = max(max_sum,num-i+1)
        return max_sum