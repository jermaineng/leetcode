class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        numsSet = set(nums) # faster than checking array
        minNum = min(nums)
        maxNum = max(nums)

        ans = []
        for i in range(minNum + 1, maxNum):
            if i not in numsSet:
                ans.append(i)

        return ans
