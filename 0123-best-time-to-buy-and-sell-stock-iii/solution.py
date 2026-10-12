class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        dp = [[[float('-inf')] * 2 for _ in range(3)] for _ in range(n)]

        dp[0][0][0] = 0
        dp[0][0][1] = -prices[0] # if buy on day 0

        for i in range(1, n):
            for j in range(2):
                dp[i][0][0] = 0

                dp[i][j][1] = max(dp[i - 1][j][0] - prices[i], dp[i - 1][j][1]) # buy/wait
                dp[i][j + 1][0] = max(dp[i - 1][j][1] + prices[i], dp[i - 1][j + 1][0]) # sell/wait
        
        return max(dp[n - 1][j][0] for j in range(3))

# dp[i][j][k] is profits earned as of curr day i after j sold transactions where k represents stock held (1) or not (0)
# can buy, sell or hold/wait
# if stock is not held, then buy or wait: dp[i][j][1] = max(dp[i - 1][j][0] - prices[i], dp[i - 1][j][1])
# if stock is held, then sell or wait: dp[i][j + 1][0] = max(dp[i][j][1] + prices[i], dp[i - 1][j + 1][0])
