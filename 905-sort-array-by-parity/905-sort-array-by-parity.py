class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
#         odd = []
#         even = []*len(nums)
#         for i in range(len(nums)):
#             if nums[i] % 2 == 0:
#                 even.append(nums[i])
#             else:
#                 odd.append(nums[i])
        
#         for i in range(len(odd)):
#             even.append(odd[i])
#         return even
        
        i,j = 0,len(nums)-1
        while i <= j:
            if nums[i]%2 != 0 and nums[j]%2 == 0:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
                j -= 1
            elif nums[i]%2 == 0 and nums[j]%2 == 0:
                i += 1
            elif nums[i]%2 != 0 and nums[j]%2 != 0:
                j -= 1
            else:
                i += 1
                j -= 1
        return nums