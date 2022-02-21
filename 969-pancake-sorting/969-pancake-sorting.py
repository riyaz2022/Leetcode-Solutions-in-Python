class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = []
        #use for loop to iterate through all nums
        for i in range(n):
            curMax = max(arr[0:n-i]) #find maximum element in range 0->last,0->last-1
            
            j = 0
            while arr[j] != curMax: #find index of max Element
                j += 1
            
            arr[0:j+1] = reversed(arr[0:j+1]) #reverse array from 0->curMax
            res.append(j+1)
            
            arr[0:n-i] = reversed(arr[0:n-i]) #now again reverse from 0->last,0->last-1
            res.append(n-i)
        
        return res
            