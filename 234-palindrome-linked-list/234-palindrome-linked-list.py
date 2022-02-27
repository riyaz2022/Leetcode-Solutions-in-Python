# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
        
        while node:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True
        # p = head
        # s = ""
        # while p:
        #     s += str(p.val)
        #     p = p.next
        # return s == s[::-1]
#         p = head
#         s = []
#         while p:
#             s.append(p.val)
#             p = p.next
        
#         p = head
#         while p:
#             data = s.pop()
#             if data != p.val:
#                 return False
#             p = p.next
#         return True
        
#         if head:
#             p = q = head
#             prev = []
#             i = 0
#             while q:
#                 prev.append(q.val)
#                 q = q.next
#                 i += 1
            
#             count = 1
#             while count <= i//2 + 1:
#                 if prev[-count] != p.val:
#                     return False
#                 p = p.next
#                 count += 1
#             return True
#         else:
#             return False