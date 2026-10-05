class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        n = len(energyDrinkA)
        dp = [[0] * 2 for _ in range(n + 2)]        

        for i in range(n - 1, -1, -1):
            dp[i][0] = energyDrinkA[i] + max(dp[i + 1][0], dp[i + 2][1])
            dp[i][1] = energyDrinkB[i] + max(dp[i + 1][1], dp[i + 2][0])

        return max(dp[0])  

# dp[i][j] represents energy boost at time i and j is energy drink type
# dp[i][0] = energyDrinkA[i] + max(dp[i + 1][0], dp[i + 2][1])
# dp[i][1] = energyDrinkB[i] + max(dp[i + 1][1], dp[i + 2][0])
# take max
