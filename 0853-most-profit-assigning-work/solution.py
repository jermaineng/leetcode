class Solution:
    def maxProfitAssignment(self, difficulty: list[int], profit: list[int], worker: list[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        worker.sort()

        total = 0
        curr_profit = 0
        i = 0

        for w in worker:
            while i < len(jobs) and jobs[i][0] <= w:
                curr_profit = max(curr_profit, jobs[i][1])
                i += 1
            
            total += curr_profit

        return total

# greedy
# sort difficulty with profit zip
# sort workers to start from worker with least difficulty
# task difficulty can only increase from there
