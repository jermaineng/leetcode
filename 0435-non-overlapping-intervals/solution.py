class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        end = intervals[0][1]
        count = 0

        n = len(intervals)
        for i in range(1, n):
            if intervals[i][0] < end:
                count += 1
            else:
                end = intervals[i][1]
        
        return count

# sort by end time
# [1,2], [1,3], [2,3], [3,4]
# [1,11], [2,12], [11,22], [1,100]
# check start time with most recently kept end point
