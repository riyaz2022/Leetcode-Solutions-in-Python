class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j] and abs(i - j) <= k:
        #             print(i,j)
        #             return True
        # return False
        dic = {}
        for i,num in enumerate(nums):
            if num in dic and i - dic[num] <= k:
                return True
            dic[num] = i
        return False
        