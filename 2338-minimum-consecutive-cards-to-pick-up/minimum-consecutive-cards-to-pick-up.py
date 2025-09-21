class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        n = len(cards)
        store = {}
        min_w = float("inf")
        for r, card in enumerate(cards):
            if card in store:
                min_w = min(min_w, r - store[card] + 1)
            store[card] = r

        return -1 if min_w == float("inf") else min_w