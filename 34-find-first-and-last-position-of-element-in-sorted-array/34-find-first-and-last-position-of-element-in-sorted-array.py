def bs(nums,target,findMaxIndex):
    keyIndex = -1
    l,h = 0,len(nums)-1
    while l <= h:
        m = (l+h)//2
        if nums[m] > target:
            h = m-1
        elif nums[m] < target:
            l = m + 1
        else:
            keyIndex = m
            if findMaxIndex:
                l = m +1
            else:
                h = m-1
    return keyIndex
    
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        range = [-1,-1]
        range[0] = bs(nums,target,False)
        if range[0] != -1:
            range[1] = bs(nums,target,True)
        return range