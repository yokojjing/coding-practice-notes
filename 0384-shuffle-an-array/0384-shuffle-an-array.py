import random
class Solution:

    def __init__(self, nums: List[int]):
        self.list = nums.copy()

    def reset(self) -> List[int]:
        return self.list.copy()

    #fisher-yates algorithm
    def shuffle(self) -> List[int]:
        result = self.list.copy()
        for i in range(len(result)):
            j = random.randint(i,len(result)-1)
            result[i],result[j] = result[j],result[i]
        return result


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()