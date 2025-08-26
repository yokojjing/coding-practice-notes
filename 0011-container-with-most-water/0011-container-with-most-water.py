class Solution:
    def maxArea(self, height: List[int]) -> int:
        curr_max = 0
        left = 0
        right = len(height)-1
        while left < right:
            if height[left] > height[right]:
                curr_max = max(curr_max,height[right]*(right-left))
                right -= 1
            else:
                curr_max = max(curr_max,height[left]*(right-left))
                left += 1
        return curr_max