class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = set()
        shrinker = 0
        max_window_length = 0

        for idx in range(len(s)):
            while s[idx] in sett:
                sett.remove(s[shrinker])
                shrinker += 1
            sett.add(s[idx])
            current_window_length = idx - shrinker + 1
            max_window_length = max(max_window_length, current_window_length)
        return max_window_length
