# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        def dfs(left,right):
            if left > right:
                return None
            m = (left+right)//2
            root = TreeNode(nums[m])
            root.left = dfs(left,m-1)
            root.right = dfs(m+1,right)
            return root
        
        return dfs(0,len(nums)-1)