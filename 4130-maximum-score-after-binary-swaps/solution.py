class Solution:
    def maximumScore(self, nums: List[int], s: str) -> int:
        heap = [] # max heap
        score = 0

        for num, ch in zip(nums, s):
            heapq.heappush(heap, -num)
            
            if ch == "1":
                score += -heapq.heappop(heap)
        
        return score

# "1"s can only move towards start of arr
# as you iterate through the arr:
    # push the number in the max heap
    # if encounter "1", pop

# basically popping gives the max remaining num from i = 0 to i = curr "1" of nums
