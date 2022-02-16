# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return None
        q = deque()
        q.append((root,0,0))
        nodeMap = defaultdict()
        while q:
            node,level,parent = q.popleft()
            nodeMap[node.val] = [level,parent]
            if node.left:
                q.append((node.left,level+1,node.val))
            if node.right:
                q.append((node.right,level+1,node.val))
        print(nodeMap)
        if nodeMap[x][0] == nodeMap[y][0] and nodeMap[x][1] != nodeMap[y][1]:
            return True
        return False
            
            
            