# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root,root.val)]
        ans = []
        while stack:
            node,maxV = stack.pop()
            if node.val >= maxV:
                ans.append(node.val)
                maxV = node.val
            if node.right:
                stack.append((node.right,maxV))
            if node.left:
                stack.append((node.left,maxV))
        return len(ans)