class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner, loser = zip(*matches)
        los_count = Counter(loser)
        answer = [[],[]]
        for nums, count in los_count.items():
            if count == 1:
                answer[1].append(nums)

        losers_set = set(loser)
        for num in set(winner):
            if num not in losers_set:
                answer[0].append(num)
        for arr in answer:
            arr.sort()
        return answer