class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        maxx = 0
        for i in range(len(points) - 1):
            diff = abs(points[i][0] - points[i+1][0])
            maxx = max(maxx, diff)
        return maxx