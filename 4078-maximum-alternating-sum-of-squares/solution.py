class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=abs)
        n = len(nums)
        mid = n // 2
        score = 0 

        for i in range(n - 1, mid - 1, -1):
            score += nums[i] * nums[i]

        for i in range(0, mid):
            score -= nums[i] * nums[i]

        return score

# -1, 1, -2, 2, -3, 3
