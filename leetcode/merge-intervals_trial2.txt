class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort()
        k = 0
        for idx in range(1, len(intervals)):
            first, last = intervals[idx]
            if first <= intervals[k][1]:
                intervals[k][1] = max(intervals[k][1], last)
            else:
                k += 1
                intervals[k] = intervals[idx]
                
        return intervals[:k+1]