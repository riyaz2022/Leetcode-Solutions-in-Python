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
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        a1 = inOrder(root1)
        print(a1)
        a2 = inOrder(root2)
        print(a2)
        if not a1:
            return a2
        if not a2:
            return a1
        m = len(a1)
        n = len(a2)
        i = j = k =0
        ans = [None]*(m+n)
        while i < m and j < n:
            if a1[i] < a2[j]:
                ans[k] = a1[i]
                i += 1
                k += 1
            else:
                ans[k] = a2[j]
                j += 1
                k += 1
        while i < m:
            ans[k] = a1[i]
            i += 1
            k += 1
        while j < n:
            ans[k] = a2[j]
            j += 1
            k += 1
        return ans
                
        