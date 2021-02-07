class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        intervals.sort(key = lambda x: x[1])
        n, count = len(intervals), 1
        if n == 0: return 0
        curr = intervals[0]
        
        for i in range(n):
            if curr[1] <= intervals[i][0]:
                count += 1
                curr = intervals[i]
                
        return n - count"""
        
        if not intervals: return 0
        intervals.sort(key=lambda x: x[0])  # sort on start time
        currEnd, cnt = intervals[0][1], 0
        for x in intervals[1:]:
            if x[0] < currEnd:  # find overlapping interval
                cnt += 1
                currEnd = min(currEnd, x[1])  # erase the one with larger end time
            else:
                currEnd = x[1]   # update end time
        return cnt