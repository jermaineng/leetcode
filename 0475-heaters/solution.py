class Solution:
    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        houses.sort()
        heaters.sort()
        n = len(houses)
        
        def can_mid(mid):
            j = 0

            for house in houses:
                while j < len(heaters) and house - mid > heaters[j]:
                    j += 1
                
                if j == len(heaters) or heaters[j] > house + mid:
                    return False
                
            return True
        
        left = 0
        right = 10**9
        rad = 0

        while left <= right:
            mid = (left + right) // 2

            if can_mid(mid):
                rad = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return rad

# use bsta
# alternatively: use two pointers (one at house, one at heater)
