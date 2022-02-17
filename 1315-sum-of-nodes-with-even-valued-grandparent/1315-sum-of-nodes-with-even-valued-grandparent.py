# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root:
            return None
        q = collections.deque()
        q.append((root,None,None))
        res = 0
        while q:
            node,parent,grandparent = q.popleft()
            if grandparent and grandparent.val%2 == 0:
                res += node.val
            if node.left:
                q.append((node.left,node,parent))
            if node.right:
                q.append((node.right,node,parent))
        return res