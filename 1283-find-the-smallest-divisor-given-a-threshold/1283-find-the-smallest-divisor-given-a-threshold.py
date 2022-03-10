class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def isPossible(size):
            ans = 0
            for num in nums:
                ans += math.ceil(num/size)
            if ans <= threshold:
                return True
            else:
                return False
        
        l,h = 1,max(nums)
        while l < h:
            mid = (l+h)//2
            if isPossible(mid):
                h = mid
            else:
                l = mid + 1
        return l