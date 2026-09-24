class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            digits_sum = 0

            while num:
                digits_sum += num % 10
                num //= 10
            
            if digits_sum == i:
                return i
        
        return -1
