class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        sum_sq = 0
        n = len(nums)

        for i in range(n):
            distinct = set()

            for j in range(i, n):                
                distinct.add(nums[j])
                count = len(distinct)
                sum_sq += count * count

        return sum_sq 
 
# iterate through using two nested loops
# use a set to keep track of distinct elements where count is len(set)
