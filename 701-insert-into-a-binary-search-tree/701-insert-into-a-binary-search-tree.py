# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        cur,next = None,root
        while next:
            cur = next
            if cur.val < val:
                next = cur.right
            else:
                next = cur.left
        
        if cur.val > val:
            cur.left = TreeNode(val)
        else:
            cur.right = TreeNode(val)
        
        return root
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if not root:
        #     return TreeNode(val)
        # if root.val > val:
        #     root.left = self.insertIntoBST(root.left,val)
        # else:
        #     root.right = self.insertIntoBST(root.right,val)
        # return root