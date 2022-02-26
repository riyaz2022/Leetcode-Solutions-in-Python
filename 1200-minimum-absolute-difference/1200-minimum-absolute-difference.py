class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans = []
        minPairDiff = float('inf')
        for i in range(len(arr)-1):
            diff = arr[i+1]-arr[i]
            if diff == minPairDiff:
                ans.append([arr[i],arr[i+1]])
            elif diff < minPairDiff:
                ans = [[arr[i],arr[i+1]]]
                minPairDiff = diff
        
        return ans
#         arr.sort()
#         res = []
        
#         minPair = float('inf')
        
#         for i in range(len(arr)-1):
#             minPair = min(minPair,arr[i+1]-arr[i])
            
#         for i in range(len(arr)-1):
#             if abs(arr[i]-arr[i+1]) == minPair:
#                 res.append([arr[i],arr[i+1]])
        
#         return res
        
        