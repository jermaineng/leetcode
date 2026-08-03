class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        ans = ["Bob", "Tie", "Alice"]
        n = len(stoneValue)
        dp = [0, 0, 0, 0]

        for i in range(n - 1, -1, -1):
            dp[i & 3] = -5e7
            total = 0

            for j in range(1, 4):
                if i + j <= n:
                    total += stoneValue[i + j - 1]
                    dp[i & 3] = max(dp[i & 3], total - dp[(i + j) & 3])

        return ans[(dp[0] > 0) - (dp[0] < 0) + 1]
