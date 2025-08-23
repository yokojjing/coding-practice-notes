class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = {'(':')','[':']','{':'}'}
        for i in s:
            if i in open:
                stack.append(open[i])
            elif stack and i == stack[-1]:
                stack.pop()
            else:
                return False
        return not stack