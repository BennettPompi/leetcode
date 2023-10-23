from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def checkSpeed(speed, h = h,piles = piles):
            if sum([ceil(x/speed) for x in piles]) <= h:
                return True
            else: return False
        if len(piles) == h:
            return max(piles)
        maxSpd = max(piles)
        minSpd = ceil(maxSpd/h)
        while maxSpd != minSpd:
            i = (maxSpd + minSpd)//2
            if checkSpeed(i):
                maxSpd = i
            else:
                minSpd = i+1
        return minSpd


