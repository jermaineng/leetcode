class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1 # empty tree
        dp[1] = 1 # one node

        for i in range(2, n + 1):
            dp[i] = 0

            for root in range(1, i + 1):
                left = root - 1
                right = i - root

                dp[i] += dp[left] * dp[right]

        return dp[n]
