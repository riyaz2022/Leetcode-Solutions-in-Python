# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        def helper(root,d):
            if not root:
                return 0
            left = helper(root.left,d)
            right = helper(root.right,d)
            subTreeSum = left + right + root.val
            d[subTreeSum] = d.get(subTreeSum,0) + 1
            return subTreeSum
        
        d = {}
        helper(root,d)
        ans = []
        mostFreq = 0
        for key in d:
            if d[key] > mostFreq:
                mostFreq = d[key]
                ans = [key]
            elif d[key] == mostFreq:
                ans.append(key)
        return ans
        