class Solution:
    def maximumScore(self, nums: list[int], multipliers: list[int]) -> int:
        n, m = len(nums), len(multipliers)
        dp = [[float('-inf')] * (m + 1) for _ in range(m + 1)]

        dp[0][0] = 0

        for i in range(1, m + 1):
            for j in range(i + 1): # number of elements taken from left cant be greater than operation count
                if j == 0: # only took from right
                    dp[i][j] = nums[n - (i - j)] * multipliers[i - 1] + dp[i - 1][j]

                elif j == i:
                    dp[i][j] = nums[j - 1] * multipliers[i - 1] + dp[i - 1][j - 1]

                else:
                    dp[i][j] = max(nums[j - 1] * multipliers[i - 1] + dp[i - 1][j - 1], 
                                    nums[n - (i - j)] * multipliers[i - 1] + dp[i - 1][j])
    
        return max(dp[m])

# dp[i][j] represents score after i operations with j elements taken from left
# dp[i][j] = max(nums[j] * multiplier[i - 1] + dp[i- 1][j - 1], nums[n - 1 - (i - j)] * multiplier[i - 1] + dp[i - 1][j])
