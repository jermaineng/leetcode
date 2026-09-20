class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return -1 if dp[amount] == float('inf') else dp[amount]

# dp[n] = min(dp[n], dp[n - i] + 1) where n represents the amt
