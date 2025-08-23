class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        new = sorted(nums)
        cur_sum = 0
        current = float(-inf)
        max_sum = float(-inf)
        for i in new:
            if i == current:
                continue
            elif i == current+1:
                cur_sum += 1
            else:
                max_sum = max(max_sum,cur_sum)
                cur_sum = 1
            current = i
        return max(max_sum,cur_sum)