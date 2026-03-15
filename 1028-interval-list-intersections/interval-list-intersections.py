class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        hold = 0
        seek = 0
        res = []
        while hold < len(firstList) and seek < len(secondList):
            start = max(firstList[hold][0], secondList[seek][0])
            end = min(firstList[hold][1], secondList[seek][1])

            if start <= end:
                res.append([start, end])

            if firstList[hold][1] < secondList[seek][1]:
                hold += 1
            else:
                seek += 1
        return res