class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        i = 0
        j = 0
        while i < len(word1) and j < len(word2):
            result += word1[i] + word2[j]
            i += 1
            j += 1
        result += word1[i:] + word2[j:]
        return result