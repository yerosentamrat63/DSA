class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        pair = 0
        window_leng = 1

        for right in range(1, n):
            if s[right] == s[right-1]:
                pair += 1

            while pair > 1:
                if s[left] == s[left + 1]:
                    pair -= 1
                left += 1
            window_leng = max(window_leng, right - left + 1)

        return window_leng