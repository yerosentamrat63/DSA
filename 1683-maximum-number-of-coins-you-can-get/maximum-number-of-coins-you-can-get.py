class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        me = 0
        piles.sort(reverse = True)
        for i in range(1, n-n//3, 2):
            me += piles[i]
        return me