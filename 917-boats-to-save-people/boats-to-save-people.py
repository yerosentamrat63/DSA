class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people) - 1
        boats = 0
        
        while l <= r:
            targ = limit - people[r]
            r -= 1
            if l <= r and targ >= people[l]:
                l += 1
            boats += 1
        return boats