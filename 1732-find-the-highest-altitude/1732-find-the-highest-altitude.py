class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curSum = 0
        maxSum = 0
        for g in gain:
            curSum += g
            if curSum > maxSum:
                maxSum = curSum
        return maxSum