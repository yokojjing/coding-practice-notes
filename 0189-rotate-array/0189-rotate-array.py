class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        #space-complexity: O(1)
        def reverse(list,left,right):
            left,right
            while left < right:
                list[left],list[right] = list[right],list[left]
                left += 1
                right -= 1
        k = k%len(nums)
        reverse(nums,0,len(nums)-1)
        reverse(nums,0,k-1)
        reverse(nums,k,len(nums)-1)
        