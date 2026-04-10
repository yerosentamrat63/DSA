class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        target = tickets[k]

        for idx in range(len(tickets)):
            if idx <= k:
                res += min(tickets[idx], target)
            else:
                res += min(tickets[idx], target - 1)

        return res