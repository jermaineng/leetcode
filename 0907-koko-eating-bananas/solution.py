class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        total = sum(piles)
        left = ceil(total / h)
        right = max(piles)

        while left < right:
            mid = (left + right) // 2

            hours = 0
            for pile in piles:
                hours += ceil(pile / mid)
            
            if hours <= h:
                right = mid
            else:
                left = mid + 1
        
        return left

# binary search on ans
# largest possible k is max of piles
# smallest possible k is ceiling of total / h
