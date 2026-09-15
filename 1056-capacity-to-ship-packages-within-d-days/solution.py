class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)  

        while left < right:
            mid = (left + right) // 2
            weight_sum = 0
            d = 1 # curr number of days needed

            for w in weights:
                if weight_sum + w > mid:
                    d += 1
                    weight_sum = w
                else:
                    weight_sum += w
                
                if d > days:
                    break
            
            if d > days:
                left = mid + 1
            else:
                right = mid
        
        return left

# bsta
# iterate through weights to see if this package can be shipped tdy, if exceed capacity (mid), then need to move package to new day
# if curr ship capacity requires > k days: increase ship capacity (i.e. left = mid + 1)
# otherwise can decrease ship capacity (i.e. right = mid)
