class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)] 

        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if length == 1:
                    dp[i][j] = 1

                elif s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2

                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        
        return dp[0][n - 1]

# dp[i][j] represents longest length of palindromic subseq s[i ... j] 
# given a palindrome subsequence s[i ... j]
# can extend if s[i - 1] == j[i + 1]
