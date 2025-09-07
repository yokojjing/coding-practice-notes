class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def minimum(left,right):
            if left == right:
                return False
            
            mid = (left+right)//2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            
            left_min = minimum(left,mid)
            right_min = minimum(mid+1,right)
            if type(left_min) is not int and type(right_min) is not int:
                return False
            if type(left_min) is int:
                return left_min
            if type(right_min) is int:
                return right_min
        
        result = minimum(0,len(nums)-1)
        if result is False:
            return nums[0]
        else:
            return result