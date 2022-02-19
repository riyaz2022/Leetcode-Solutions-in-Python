class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        level = nodeCount = 1
        while label >= nodeCount*2:
            nodeCount *= 2
            level += 1
        
        ans = []
        while label != 0:
            ans.append(label)
            levelMax = 2**(level)-1
            levelMin = 2**(level-1)
            label = int((levelMax + levelMin - label)/2)
            level -= 1
        return ans[::-1]