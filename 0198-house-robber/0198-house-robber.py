class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        prev = nums[0]
        current = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            temp = max(prev+nums[i],current)
            prev = current
            current = temp
        return current