# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        q = collections.deque()
        q.append(root)
        ans = []
        while q:
            level = []
            maxR = -float('inf')
            for _ in range(len(q)):
                node = q.popleft()
                maxR = max(maxR,node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(maxR)
        return ans