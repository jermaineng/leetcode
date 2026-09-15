class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)

        while left < right:
            curr_sum = 0
            count = 1
            mid = (left + right) // 2

            for num in nums:
                if curr_sum + num > mid:
                    count += 1
                    curr_sum = num
                else:
                    curr_sum += num

                if count > k:
                    break

            if count > k:
                left = mid + 1 # mid (ans) is too small
            else:
                right = mid

        return left      

# binary search on the sum where max is sum of entire array (subarray is entire array), min is max num from array (subarray has only one number)
# if curr num is infeasible: left = mid + 1 
# otherwise right = mid

# feasibility: iterate through nums, whenever curr sum > mid: increase subarray count
