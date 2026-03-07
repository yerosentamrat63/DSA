class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        left_p = 0
        left_t = 0
        count = 0
        while left_p < len(players) and left_t < len(trainers):
            if players[left_p] <= trainers[left_t]:
                count += 1
                left_p += 1
                left_t += 1
            else:
                left_t += 1
        return count