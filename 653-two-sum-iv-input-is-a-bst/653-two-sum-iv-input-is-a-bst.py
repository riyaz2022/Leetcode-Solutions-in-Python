# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        stack = [root]
        seen = set()
        while stack:
            cur = stack.pop()
            if k-cur.val in seen:
                return True
            seen.add(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return False
    #Can also be done via inOrder travsersal(result in a sorted array) first and simple two sum on sorted array