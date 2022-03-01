# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast =slow= head
        maxV = 0
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        cur = slow
        prev = None
        while cur:
            cur.next,prev,cur = prev,cur,cur.next
        
        while prev:
            maxV = max(maxV,head.val+prev.val)
            head = head.next
            prev = prev.next
        
        return maxV
        
            
#         cur = head
#         ans = []
#         length = 0
#         while cur:
#             ans.append(cur.val)
#             cur = cur.next
#             length += 1
        
#         maxA = 0
#         i,j = 0,length-1
#         while i < j:
#             maxA = max(maxA, ans[i]+ans[j])
#             i += 1
#             j -= 1
#         return maxA
        