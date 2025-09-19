class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        max_count, current_count = 0, 0

        for i in range(k):
            if s[i] in vowels:
                current_count += 1
        max_count = current_count

        for i in range(k, len(s)):
            if s[i - k] in vowels:
                current_count -= 1
            if s[i] in vowels:
                current_count += 1
            max_count = max(current_count, max_count)
        return max_count