class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        xs = []
        for i in range(len(points)):
            for j in range(1):
                xs.append(points[i][j])
                break
        xs.sort()
        max = 0
        i = 0
        while i + 1 < len(xs):
            if xs[i + 1] - xs[i] > max:
                max = xs[i + 1] - xs[i]
            i += 1
        return(max)