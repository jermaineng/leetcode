class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def rob_max(houses):
            n = len(houses)
            dp = [0] * (n + 1)

            dp[1] = houses[0]

            for i in range(2, n + 1):
                dp[i] = max(dp[i - 1], dp[i - 2] + houses[i - 1])
            
            return dp[n]
        
        return max(rob_max(nums[:-1]), rob_max(nums[1:]))
        # first represents robbing first house so cannot rob last
        # second represents not robbing first

# dp[i] represents max amt from first i houses
