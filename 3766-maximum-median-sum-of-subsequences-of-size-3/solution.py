class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        n = len(nums)
        median_sum = 0

        nums.sort(reverse=True)

        k = len(nums) // 3

        for i in range(k):
            median_sum += nums[2 * i + 1]

        return median_sum
