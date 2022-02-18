# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def inOrder(root):
    if not root:
        return None
    ans = []
    stack = [(root,False)]
    while stack:
        node,v = stack.pop()
        if v == True:
            ans.append(node.val)
        else:
            if node.right:
                stack.append((node.right,False))
            stack.append((node,True))
            if node.left:
                stack.append((node.left,False))
    return ans
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nums = inOrder(root)
        def dfs(left,right):
            if left > right:
                return None
            m = (left+right)//2
            root = TreeNode(nums[m])
            root.left = dfs(left,m-1)
            root.right = dfs(m+1,right)
            return root
        
        return dfs(0,len(nums)-1)