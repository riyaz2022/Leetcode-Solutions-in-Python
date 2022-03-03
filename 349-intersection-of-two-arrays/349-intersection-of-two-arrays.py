class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        m = {}
        for i in range(len(nums1)):
            if nums1[i] not in m:
                m[nums1[i]] = 0
            m[nums1[i]] += 1
            
        for i in nums2:
            if i in m:
                ans.append(i)
                del m[i]
        
        return ans