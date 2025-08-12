# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list1 = []
        while head:
            list1.append(head.val)
            head = head.next
        left,right = 0,len(list1)-1
        while left < right:
            if list1[left] != list1[right]:
                return False
            left += 1
            right -= 1
        return True