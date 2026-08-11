class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prefix_sum = nums[0]
        n = len(nums)

        for i in range(1, n):
            if nums[i] != nums[i - 1] + 1:
                break
            prefix_sum += nums[i]
        
        nums_set = set(nums)

        while prefix_sum in nums_set:
            prefix_sum += 1
        
        return prefix_sum
