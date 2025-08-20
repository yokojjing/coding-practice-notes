class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        current_max = 0
        global_max = float(-inf)
        for num in nums:
            if current_max + num > num:
                current_max += num
            else:
                current_max = num
            if global_max <= current_max:
                global_max = current_max
        return global_max
            