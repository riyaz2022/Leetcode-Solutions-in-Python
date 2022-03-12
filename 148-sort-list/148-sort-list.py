# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = []
        while head:
            ans.append(head.val)
            head = head.next
        
        ans.sort()
        cur = dummy = ListNode(0)
        for e in ans:
            cur.next = ListNode(e)
            cur = cur.next
            
        return dummy.next
            