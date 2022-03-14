# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        res = []
        while head:
            while stack and stack[-1][1] < head.val:
                res[stack.pop()[0]] = head.val
            stack.append((len(res),head.val))
            res.append(0)
            head = head.next
        return res
#         if not head:
#             return None
#         ans = []
#         while head:
#             ans.append(head.val)
#             head = head.next
#         stack = []
#         res = [0]*len(ans)
#         for i in range(len(ans)):
#             while stack and ans[stack[-1]] < ans[i]:
#                 res[stack.pop()] = ans[i]
#             stack.append(i)
        
#         return res
#         if not head:
#             return None
#         answer = []
#         while head:
#             cur = head
#             while cur and cur.val <= head.val:
#                 cur = cur.next
#             if not cur:
#                 answer.append(0)
#             else:
#                 answer.append(cur.val)
#             head = head.next
        
#         return answer
            