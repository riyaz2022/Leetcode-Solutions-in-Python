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
        node,flag = stack.pop()
        if flag == True:
            ans.append(node.val)
        else:
            if node.right:
                stack.append((node.right,False))
            stack.append((node,True))
            if node.left:
                stack.append((node.left,False))
    return ans
    
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        array = inOrder(root)
        print(array)
        return array[k-1]