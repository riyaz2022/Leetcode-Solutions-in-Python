class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def count(d):
            ans = 1
            cur = position[0]
            for i in range(1,len(position)):
                if position[i] - cur >= d:
                    ans += 1
                    cur = position[i]
            return ans
        
        l,h = 1,position[-1] - position[0]
        while l < h:
            mid = h - (h-l)//2
            if count(mid) >= m:
                l = mid
            else:
                h = mid-1
        
        return l