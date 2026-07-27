class Solution:
    def climbStairs(self, n: int) -> int:
        # fibonacci sequence (ways[n] = ways[n - 1] + ways[n - 2])
        if n == 1:
            return 1

        prev1 = prev2 = 1

        for _ in range(2, n + 1):
            prev1, prev2 = prev2, prev1 + prev2
        
        return prev2


