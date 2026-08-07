from math import ceil

class Solution:
    def totalhours(self, speed, piles):
        hours = 0
        for pile in piles:
            hours += ceil(pile / speed)
        return hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        while low < high:
            mid = low + (high - low) // 2

            if self.totalhours(mid, piles) <= h:
                high = mid
            else:
                low = mid + 1

        return low