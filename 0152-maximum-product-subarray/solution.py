class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # If positive, we take, and multiply by largest f(i-1)
        # Otherwise, don't know if we need to take or not.
        
        # n = len(nums)
        # memo = {}
        
        # def f(i, j):
        #     if i <= 0:
        #         return 1
        #     if (i, j) in memo:
        #         return memo[(i, j)]
        #     val = nums[i-1]
        #     if j == 0:
        #         # maximum
        #         res = max(f(i-1, 0) * val, val, f(i-1, 1) * val)
        #         memo[(i, j)] = res
        #         return res
        #     else:
        #         res = min(f(i-1, 1) * val, val, f(i-1, 0) * val)
        #         memo[(i, j)] = res
        #         return res
                
        # return max(f(i, 0) for i in range(1, n+1))
        
        # dp[i] keeps track of max prod ending at index i
        # either multiply by next num or start new
        # for positive we want largest, 
            # dp[i] = max(dp[i - 1] * nums[i], nums[i])
        # for negative smallest
            # dp[i] = min(dp[i - 1] * nums[i], nums[i])
        # depending on whether nums[i] is pos or neg, we want largest or smallest prod
        
        n = len(nums)
        dp_max = [float('-inf')] * (n)
        dp_min = [float('inf')] * (n)
        
        dp_max[0] = nums[0]
        dp_min[0] = nums[0]
        
        for i in range(1, n):
            dp_max[i] = max(dp_max[i - 1] * nums[i], nums[i], dp_min[i - 1] * nums[i])
            dp_min[i] = min(dp_min[i - 1] * nums[i], nums[i], dp_max[i - 1] * nums[i])
        
        return max(dp_max) 
