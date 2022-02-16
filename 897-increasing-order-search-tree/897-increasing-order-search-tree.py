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
        if node:
            if v == True:
                ans.append(node)
            else:
                if node.right:
                    stack.append((node.right,False))
                stack.append((node,True))
                if node.left:
                    stack.append((node.left,False))
    return ans
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        tempArray = inOrder(root)
        for i in range(len(tempArray)-1):
            tempArray[i].left = None
            tempArray[i].right = tempArray[i+1]
        tempArray[-1].left = None
        tempArray[-1].right = None
        
        return tempArray[0]