class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        smaller = 0
        count = 0

        for num in nums:
            if num == target:
                count += 1
            elif num < target:
                smaller += 1

        return [smaller + i for i in range(count)]

# count how many numbers are smaller than it
# as well as how many of target are there present in nums
