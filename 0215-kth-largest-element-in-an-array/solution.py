class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, num)

            if len(heap) > k:
                heapq.heappop(heap) # remove smallest number from heap

        return heapq.heappop(heap)

# use max heap of size k
# pop after finish iterating
