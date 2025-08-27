# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next:
            return head
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow
        prev = slow
        cur = slow.next
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        backwards = prev
        back_next = prev.next
        forwards = head
        for_next = head.next
        while forwards != mid:
            forwards.next = backwards
            if backwards == mid:
                backwards.next = None
            else:
                backwards.next = for_next
            temp = for_next.next
            forwards = for_next
            for_next = temp
            backwards = back_next
            if back_next:
                back_next = back_next.next
        if forwards.next:
            forwards.next = None
        return head