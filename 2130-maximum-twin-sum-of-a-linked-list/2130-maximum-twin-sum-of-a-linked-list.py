# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        cur = head
        ans = []
        length = 0
        while cur:
            ans.append(cur.val)
            cur = cur.next
            length += 1
        
        maxA = 0
        i,j = 0,length-1
        while i < j:
            maxA = max(maxA, ans[i]+ans[j])
            i += 1
            j -= 1
        return maxA
        