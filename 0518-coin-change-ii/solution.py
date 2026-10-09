class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        n = len(coins)
        dp = [0] * (amount + 1)

        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        
        return dp[amount]

# dp[i] measures number of distinct ways to make i amount using coins so far
# dp[i] += dp[i - c]

# # top down:
# class Solution:
#     def change(self, amount: int, coins: list[int]) -> int:
#         n = len(coins)
#         memo = {}

#         def f(i, j):
#             if j == 0: # made amount
#                 return 1
#             if j < 0 or i == n: # amount exceeded or ran out of coins
#                 return 0
#             if (i, j) in memo:
#                 return memo[(i, j)]
            
#             memo[(i, j)] = f(i, j - coins[i]) + f(i + 1, j)
#             return memo[(i, j)]

#         return f(0, amount)

# f(i, j) represents number of ways made with coins from index i to end to make j amount
# f(i, j) = f(i, j - coins[i]) + f(i + 1, j)
# either use coin i again or next coin
