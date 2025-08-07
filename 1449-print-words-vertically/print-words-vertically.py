class Solution:
    def printVertically(self, s: str) -> list[str]:
        words = s.split()
        if not words:
            return []
        max_len = len(max(words, key=len))

        result = []
        for i in range(max_len):
            current_col = []
            for word in words:
                if i < len(word):
                    current_col.append(word[i])
                else:
                    current_col.append(' ')
            result.append("".join(current_col).rstrip())
        return result
            