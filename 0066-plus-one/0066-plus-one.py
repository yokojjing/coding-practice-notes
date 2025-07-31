class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            if carry != 1:
                return digits
            digits[i] += 1
            carry = digits[i] // 10
            digits[i] %= 10
        if carry != 0:
            return [carry] + digits
        return digits