# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
#         sum_list = LinkedList()
#         carry = 0
#         while l1 or l2:
#             if not l1:
#                 i = 0
#             else:
#                 i = l1.val
#             if not l2:
#                 j = 0
#             else:
#                 j = l2.val
            
#             s = i + j + carry
            
#             if s >= 10:
#                 carry = 1
#                 remainder = s%10
#                 sum_list.append(remainder)
#             else:
#                 sum_list.append(s)
            
#             if l1:
#                 l1 = l1.next
#             if l2:
#                 l2 = l2.next
#         return sum_list
            carry = 0
            root = n = ListNode(0)
            while l1 or l2 or carry:
                v1 = v2 = 0
                if l1:
                    v1 = l1.val
                    l1 = l1.next
                if l2:
                    v2 = l2.val
                    l2 = l2.next
                carry, val = divmod(v1+v2+carry, 10)
                n.next = ListNode(val)
                n = n.next
            return root.next
            