class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            num2 = target - nums[i]
            if num2 in hashMap:
                return [hashMap[num2], i]
            else:
                hashMap[nums[i]] = i
                