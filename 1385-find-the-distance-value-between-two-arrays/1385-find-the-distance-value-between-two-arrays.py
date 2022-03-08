def isValid(val,arr2,d):
    l,h = 0,len(arr2)
    while l < h:
        m = (l+h)//2
        if abs(val-arr2[m]) <= d:
            return False
        elif arr2[m] > val:
            h = m
        else:
            l = m+1
    return True
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        return sum(isValid(x,arr2,d) for x in arr1)