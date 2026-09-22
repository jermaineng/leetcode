class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        dp = [0] * k # contains number of subarrays ending at prev index
        count = [0] * k

        for num in nums:
            new_dp = [0] * k # number of subarrays ending at curr index

            new_dp[num % k] += 1 # start new subarray

            for r in range(k): # extend subarrays
                new_r = (num * r) % k
                new_dp[new_r] += dp[r]

            for r in range(k):
                count[r] += new_dp[r]

            dp = new_dp
        
        return count

# dp[i][r] = number of subarrays ending at index i with remainder r
# at every index i: can either
# 1. extend subarray
    # next r = (nums[i] * r) % k
# 2. start new subarray

# def resultArray(self, nums: List[int], k: int) -> List[int]:
    # r = nums[i] % k

    # n = len(nums)
    # dp = [[0] * k for _ in range(n)]

    # for i in range(n):
    #     dp[i][nums[i] % k] += 1

    #     if i > 0:
    #         for r in range(k):
    #             next_r = (nums[i] * r) % k
    #             dp[i][next_r] += dp[i - 1][r]
    
    # count = [0] * k
    # for i in range(n):
    #     for r in range(k):
    #         count[r] += dp[i][r]
    
    # return count

# optimise to 1d dp since we only need the count from prev index so
# dp[r] = number of subarrays ending at prev index with remainder r
