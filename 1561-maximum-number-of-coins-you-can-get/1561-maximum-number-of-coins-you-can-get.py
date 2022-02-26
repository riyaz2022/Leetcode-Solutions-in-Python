class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        ans = 0
        n = len(piles)
        for i in range(1,n-n//3,2):
            ans += piles[i]
        
        return ans
        