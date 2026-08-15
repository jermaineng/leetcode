class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        has_nonzero = False

        for num in nums:
            if num != 0:
                has_nonzero = True
            total ^= num
        
        if total != 0:
            return n
        if not has_nonzero:
            return 0
        return n - 1

# possible ans: n, n - 1, 0
# n - 1 when xor of array is 0
# 0 when all elements are 0
