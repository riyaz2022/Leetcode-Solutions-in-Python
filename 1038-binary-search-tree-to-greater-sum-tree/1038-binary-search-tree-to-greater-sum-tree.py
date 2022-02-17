# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        # def dfs(left,right):
        #     if left > right:
        #         return None
        #     m = (left+right)//2
        #     root = TreeNode(ans[m])
        #     root.left = dfs(left,m-1)
        #     root.right = dfs(m+1,right)
        #     return root
        
        # return dfs(0,len(ans)-1)
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
    def bstToGst(self, root: TreeNode) -> TreeNode:
        nums = inOrder(root)
        n = len(nums)
        ans = [0]*n
        ans[n-1] = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            ans[i] = ans[i+1] + nums[i]
        
        hash = {}
        for i in range(len(nums)):
            if nums[i] not in hash:
                hash[nums[i]] = i
        
        q = collections.deque()
        q.append(root)
        while q:
            node = q.popleft()
            node.val = ans[hash[node.val]]
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        return root
        