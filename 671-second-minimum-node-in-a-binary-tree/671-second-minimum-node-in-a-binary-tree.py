# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        q = collections.deque()
        q.append(root)
        mn,secMn = root.val,float('inf')
        while q:
            node = q.popleft()
            if node.val < secMn and node.val != mn:
                secMn = node.val
            if node.left:
                q.append(node.left)
                q.append(node.right)
        
        if secMn == float('inf'):
            return -1
        else:
            return secMn