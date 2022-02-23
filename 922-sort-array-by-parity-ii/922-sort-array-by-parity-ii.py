class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        # odd = []
        # even = []
        # for i in range(len(nums)):
        #     if nums[i]%2==0:
        #         even.append(nums[i])
        #     else:
        #         odd.append(nums[i])
        # ans = []*len(nums)
        # i = j = 0
        # while i < len(even) or j < len(odd):
        #     if len(ans)%2==0:
        #         ans.append(even[i])
        #         i += 1
        #     else:
        #         ans.append(odd[j])
        #         j += 1
        # return ans
        i,j,k = 0,1,len(nums)
        while i < k and j < k:
            if nums[i]%2 == 0:
                i += 2
            elif nums[j]%2 == 1:
                j += 2
            else:
                nums[i],nums[j] = nums[j],nums[i]
        return nums
                
                