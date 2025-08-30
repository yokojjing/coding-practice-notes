class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        min_val = max_val = result = nums[0]
        for i in range(1,len(nums)):
            if nums[i] < 0:
                min_val,max_val = max_val,min_val
            min_val = min(nums[i],min_val*nums[i])
            max_val = max(nums[i],max_val*nums[i])
            result = max(result,max_val)
        return result