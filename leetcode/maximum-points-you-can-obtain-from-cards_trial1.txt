class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        l, r = 0, n - k
        max_score = sum(cardPoints[r:])
        res = max_score

        while r < n:
            max_score += cardPoints[l]
            max_score -= cardPoints[r]
            res = max(res, max_score)
            r += 1
            l += 1
        return res   