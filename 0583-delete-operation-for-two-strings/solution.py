class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # word2 is empty
        for i in range(m + 1):
            dp[i][0] = i
        
        # word1 is empty
        for i in range(n + 1):
            dp[0][i] = i
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
        
        return dp[m][n]

# dp[i][j] represents min number of deletions for word1 index [:i] and word2[:j]
# if letters match, dp[i][j] = dp[i - 1][j - 1]
# else: dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
