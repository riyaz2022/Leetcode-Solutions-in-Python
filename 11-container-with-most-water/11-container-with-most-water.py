class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j = 0,len(height)-1
        maxW = -float('inf')
        while i < j:
            water = min(height[i],height[j])*(j-i)
            maxW = max(maxW,water)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxW