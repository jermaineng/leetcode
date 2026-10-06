class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        n = len(intervals)
        ans = [intervals[0]]

        for interval in intervals[1:]:
            if interval[0] <= ans[-1][1]: # overlap
                ans[-1][1] = max(interval[1], ans[-1][1])
            else:
                ans.append(interval)
        
        return ans

# sort intervals then compare:
# if start2 <= end1: merge
# otherwise new interval
