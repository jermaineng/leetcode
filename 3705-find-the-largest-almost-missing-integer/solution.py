class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if k == len(nums):
            return max(nums)
        
        poss_nums = nums if k == 1 else [nums[0], nums[-1]]
        valid_nums = [x for x in poss_nums if nums.count(x) == 1]
        return max(valid_nums) if valid_nums else -1
