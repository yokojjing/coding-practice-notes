class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if target - nums[i] in check:
                return [check[comp],i]
            check[nums[i]] = i
        return []
            