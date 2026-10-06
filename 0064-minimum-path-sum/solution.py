class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        r, c = len(grid), len(grid[0])
        dp = [[0] * c for _ in range(r)]

        for i in range(r):
            for j in range(c):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j] + grid[i][j], dp[i][j - 1] + grid[i][j])

        return dp[r - 1][c - 1]

# dp[i][j] represents min sum from start to position i, j
# dp[i][j] = min(dp[i - 1][j] + grid[i][j], dp[i][j - 1] + grid[i][j])
# if first row, can only come from left
# if first col, can only come from up
