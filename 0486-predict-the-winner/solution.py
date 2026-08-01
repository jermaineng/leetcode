class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)

        if n % 2 == 0:
            return True
        # player 1 can either always choose even indexes or odd indexes, i.e.
        # player 1 can at least tie
        
        dp = [0] * n
        for i in range(n - 1, -1, -1):
            dp[i] = nums[i]
            
            for j in range(i + 1, n):
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])
            
        return dp[n - 1] >= 0

# dp[i][j] stores max score diff for nums[i ... j]
