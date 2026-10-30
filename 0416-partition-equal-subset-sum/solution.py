class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)

        if total % 2 == 1: # odd sum
            return False
        
        half_sum = total // 2
        dp = [False] * (half_sum + 1)
        dp[0] = True

        for num in nums:
            for i in range(half_sum, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        return dp[half_sum]

# sum of one subset is equal to total sum // 2
# dp[i] represents whether sum i is possible using elements seen so far
# either take or dont take so dp[i] is either dp[i] or dp[i - num]
# we only keep whatever is true
