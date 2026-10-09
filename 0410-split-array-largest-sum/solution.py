class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def can_mid(mid):
            curr_sum = 0
            subarr_count = 1

            for num in nums:
                if num > mid:
                    return False
                    
                if curr_sum + num > mid:
                    subarr_count += 1
                    curr_sum = num
                else:
                    curr_sum += num
            
            return subarr_count <= k
        
        left = 0
        right = 10**9
        ans = 0

        while left <= right:
            mid = (left + right) // 2

            if can_mid(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans

# bsta
# left = 0, right = 10^6
