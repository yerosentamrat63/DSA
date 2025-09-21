class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        l = 0
        r = k - 1
        whites_count = blocks[:k].count("W")
        min_whites = whites_count
        
        while r < n - 1:
            if blocks[l] == "W":
                whites_count -= 1
            l += 1
            r += 1
            if blocks[r] == "W":
                whites_count += 1
            min_whites = min(min_whites, whites_count)
        
        return min_whites
