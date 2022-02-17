# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def traversal(root):
    stack = [(root,False)]
    ans = []
    while stack:
        node,v = stack.pop()
        if node:
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
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        a = traversal(root)
        res = []
        hash = {}
        for i in range(len(a)):
            if a[i] not in hash:
                hash[a[i]] = 0
            hash[a[i]] += 1
        
        maximum = 0
        for k,v in hash.items():
            if hash[k] > maximum:
                maximum = v
            
        for k,v in hash.items():
            if v == maximum:
                res.append(k)
        return res
                