class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        triplets = []

        for i in range(n - 2):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    triplets.append([nums[i], nums[left], nums[right]])
                    
                    # skip duplicates
                    left += 1
                    right -=1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -=1
        
        return triplets

# use three pointers
# sort then for every num i, find other two nums that sum to its negative
# one pointer is at i + i, other is at n - 1
# if too large, move right ptr. otherwise, move left ptr
