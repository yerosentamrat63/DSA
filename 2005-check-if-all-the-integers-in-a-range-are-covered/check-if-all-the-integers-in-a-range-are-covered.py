class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for i in range(left, right + 1):
            for l, r in ranges:
                if l <= i <= r:
                    break
            else:
                return False
        return True

