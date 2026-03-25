class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = Counter(p)
        win_count = Counter(s[:len(p) - 1])
        res = []

        for idx in range(len(p) - 1, len(s)):
            curr_char = s[idx]
            win_count[curr_char] += 1
            if win_count == target:
                res.append(idx - len(p) + 1)
            win_count[s[idx - len(p) + 1 ]] -= 1
            if win_count[s[idx - len(p) + 1]] == 0:
                  del win_count[s[idx - len(p) + 1]]
        return res              