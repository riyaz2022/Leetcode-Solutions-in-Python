# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def inOrder(root):
    if not root: return None
    stack = [(root,False)]
    ans = []
    while stack:
        node, flag = stack.pop()
        if flag:
            ans.append(node.val)
        else:
            if node.right:
                stack.append((node.right,False))
            stack.append((node,True))
            if node.left:
                stack.append((node.left,False))
    return ans
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = inOrder(root)
        print(arr)
        if len(arr) == 1:
            return True
        for i in range(1,len(arr)):
            if arr[i] <= arr[i-1]:
                return False
        return True