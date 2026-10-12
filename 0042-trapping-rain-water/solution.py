class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        
        left = 0
        right = n - 1
        vol = 0
        left_max, right_max = 0, 0

        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if left_max < right_max:
                vol += left_max - height[left]
                left += 1
            else:
                vol += right_max - height[right]
                right -= 1
        
        return vol

# two pointers
# keep track of left max and right max so far
# if left max < right max: take left max - curr height, then move left pointer
# else: take right max - curr height, then move right pointer
