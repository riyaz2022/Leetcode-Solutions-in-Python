class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l,h = 0,len(people)-1
        ans = 0
        while l <= h:
            if people[l] + people[h] <= limit:
                l += 1
            h -= 1
            ans += 1
        return ans