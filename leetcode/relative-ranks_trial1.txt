class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        correct = sorted(score, reverse = True)
        first = "Gold Medal"
        second = "Silver Medal"
        third = "Bronze Medal"
        res = []
        ans = {}
        for idx in range(len(correct)):
            if idx == 0:
                ans[correct[idx]] = first
            elif idx == 1:
                ans[correct[idx]] = second
            elif idx == 2:
                ans[correct[idx]] = third
            else:
                ans[correct[idx]] = str(idx+1)
        for num in score:
            res.append(ans[num])
        return res
