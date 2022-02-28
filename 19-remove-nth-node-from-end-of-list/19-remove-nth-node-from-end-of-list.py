# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head
        for _ in range(n): #travel to nth node using fast pointer
            fast = fast.next
        
        if not fast:
            return head.next
        
        while fast.next: #now as fast is nth steps ahead so when fast reaches the end
            slow = slow.next #then slow will reach the nth from end node 
            fast = fast.next
        
        slow.next = slow.next.next
        return head