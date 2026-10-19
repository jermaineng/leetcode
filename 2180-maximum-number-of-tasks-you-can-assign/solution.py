class Solution:
    def maxTaskAssign(self, tasks: list[int], workers: list[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()
        m, n = len(tasks), len(workers)

        def can_mid(mid):
            pos_tasks = deque() # deque of tasks possible with pill for this particular worker
            pill_count = 0
            i = 0

            for worker in workers[n - mid:]: # start with kth strongest workers
                while i < mid and worker + strength >= tasks[i]:
                    pos_tasks.append(tasks[i])
                    i += 1
                
                if not pos_tasks:
                    return False
                
                if pos_tasks[0] <= worker: # no need to take pill
                    pos_tasks.popleft()
                else:
                    if pill_count == pills:
                        return False

                    pill_count += 1 # take pill so must do hardest posisble task
                    pos_tasks.pop()
                
            return True       
        
        left, right = 0, min(m, n)
        ans = 0

        while left <= right:
            mid = (left + right) // 2

            if can_mid(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans

# sort workers and tasks
# bsta on k tasks to find max tasks possible with pills
