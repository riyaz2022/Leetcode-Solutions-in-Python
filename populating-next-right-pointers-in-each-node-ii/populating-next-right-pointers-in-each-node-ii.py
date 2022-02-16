"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None
        q = deque()
        q.append(root)
        while q:
            prev = None
            for _ in range(len(q)):
                cur = q.popleft()
                if prev:
                    prev.next = cur
                prev = cur
                
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return root