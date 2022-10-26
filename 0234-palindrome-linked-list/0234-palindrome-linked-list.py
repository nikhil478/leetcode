# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        l1,l2 = head,head
        
        while l2 and l2.next:
            l2 = l2.next.next
            l1 = l1.next
            
        prev = None
        
        while l1:
            nextNode = l1.next
            l1.next = prev
            prev = l1
            l1 = nextNode
            
        while prev and head:
            if prev.val != head.val:
                return False
            else:
                prev = prev.next
                head = head.next
        return True    
            
        