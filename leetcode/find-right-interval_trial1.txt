class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = [(intervals[i][0], i) for i in range(len(intervals))]
        starts.sort()

        starting_vals = [s[0] for s in starts]
        res = []
        
        for start, end in intervals:
            idx = bisect_left(starting_vals, end)
            if idx < len(intervals):
                res.append(starts[idx][1])
            else:
                res.append(-1)
        return res