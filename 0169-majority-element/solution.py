class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # moore's voting algorithm (works here because majority element appears more than n/2 times, implying other elements appear less than n/2 times)
        candidate = -1
        vote = 0

        for num in nums:
            if vote == 0:
                candidate = num
            
            if num == candidate:
                vote += 1
            else:
                vote -= 1

        return candidate

