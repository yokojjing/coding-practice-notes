from collections import defaultdict
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1,nums2 = nums2,nums1
        counter = defaultdict(int)
        result = []
        
        for i in nums1:
            counter[i] += 1

        for num in nums2:
            if counter[num] > 0:
                result.append(num)
                counter[num] -= 1
        
        return result