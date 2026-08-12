class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        max_length = 0
        freq = {}

        for right in range(n):
            curr = nums[right]
            freq[curr] = freq.get(curr, 0) + 1

            while freq[curr] > k:
                prev = nums[left]
                freq[prev] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length

# use two ptrs
# as right ptr moves, keep track of freq of nums
# once freq exceeds k, find length then move left ptr until freq no longer exceeds k
