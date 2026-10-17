class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def sum_digits(num):
            digit_sum = 0
            while num > 0:
                digit_sum += num % 10
                num //= 10

            return digit_sum

        n = len(nums)
        target = sorted(nums, key=lambda x: (sum_digits(x), x))
        pos = {num: i for i, num in enumerate(nums)} # hash map of where num curr is
        count = 0

        for i in range(n):
            if nums[i] == target[i]:
                continue
            
            idx = pos[target[i]] # find where the number that should be at position i is
            pos[nums[i]] = idx
            pos[nums[idx]] = i
            nums[i], nums[idx] = nums[idx], nums[i]
            count += 1
        
        return count

# sort into correct order
# keep hash map of where num is
# for every pos i, if wrong, find the num that belongs there and swap
