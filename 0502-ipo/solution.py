class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        projs = sorted(zip(capital, profits))

        heap = []
        i = 0
        for _ in range(k):
            while i < len(projs) and projs[i][0] <= w:
                heapq.heappush(heap, -projs[i][1])
                i += 1
                
            if not heap:
                break
                
            w += -heapq.heappop(heap)

        return w

# sort by capital
# for w amt, push all the profits in (max-heap) and pop max
# add profit to w and repeat for k projects
