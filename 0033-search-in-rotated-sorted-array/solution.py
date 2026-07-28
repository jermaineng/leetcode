class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        left = 0
        right = n - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]: # left half is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            else: # right half is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            
        return -1

# array is either entirely sorted or contains one sorted half
# [5, 6, 0, 1, 2, 3, 4]
# compare left with middle. if left > middle, right half is sorted otherwise left half is sorted
# compare target with sorted half ranges (sorted half's start and end)
# binary search in the relevant half and repeat
