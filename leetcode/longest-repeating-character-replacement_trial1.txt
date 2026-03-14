class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = defaultdict(int)
        res = 0
        left = 0

        for right in range(len(s)):
            hashmap[s[right]] += 1

            max_freq = max(hashmap.values())
            current_length = right - left + 1

            if current_length - max_freq > k:
                hashmap[s[left]] -= 1
                left += 1
                current_length = right - left + 1
            res = max(res, current_length)
        return res