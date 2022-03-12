# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None
        bef = bef_head = ListNode(0)
        aft = aft_head = ListNode(0)
        
        while head:
            if head.val < x:
                bef.next = head
                bef = bef.next
            else:
                aft.next = head
                aft = aft.next
            head = head.next
        
        aft.next = None
        bef.next = aft_head.next
        
        return bef_head.next