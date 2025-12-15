class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        expected = sorted(heights)
    # return sum(1 for i, h in enumerate(heights) if h != expected[i])
        for i, h in enumerate(heights):
            if h != expected[i]:
                count += 1
        return count
