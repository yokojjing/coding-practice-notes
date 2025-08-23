class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        lookup = set(nums)
        max_sum = 0
        for i in lookup:
            if i-1 not in lookup:
                num = i
                current = 1
                while num+1 in lookup:
                    current += 1
                    num += 1
                if current > max_sum:
                    max_sum = current
        return max_sum