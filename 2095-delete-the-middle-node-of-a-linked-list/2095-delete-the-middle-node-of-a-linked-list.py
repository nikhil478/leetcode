# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        fast,slow,fslow = head,head,head
        
        if not head or not head.next:
            return None
        
        while (fast.next and fast.next.next):
            fast = fast.next.next
            fslow = slow
            slow = slow.next
            
            
        if fast.next:
            fslow = slow
            slow = slow.next
        
        
        fslow.next = slow.next
        
        return head
        
            
            
    