import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l,r = 0, math.ceil(math.sqrt(c))
        while l <= r:
            s = l*l + r*r
            if s > c:
                r -= 1
            elif s < c:
                l += 1
            else:
                return True
        return False