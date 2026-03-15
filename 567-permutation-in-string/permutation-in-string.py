class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        count_s1 = Counter(s1)
        win = defaultdict(int)

        for right in range(len(s2)):
            win[s2[right]] += 1
            if right - left + 1 > len(s1):
                win[s2[left]] -= 1
                if win[s2[left]] == 0:
                    del win[s2[left]]
                left += 1
            if win == count_s1:
                return True

        return False