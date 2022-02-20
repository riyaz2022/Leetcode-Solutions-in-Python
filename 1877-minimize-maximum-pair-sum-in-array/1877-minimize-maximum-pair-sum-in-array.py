class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i,j = 0,len(nums)-1
        ans = []
        while i < j:
            ans.append([nums[i],nums[j]])
            i += 1
            j -= 1
        
        maxP = 0
        for x in ans:
            maxP = max(maxP,sum(x))
        return maxP
            