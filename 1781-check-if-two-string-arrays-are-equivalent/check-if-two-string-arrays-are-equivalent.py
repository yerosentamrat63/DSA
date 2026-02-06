class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        joined_word1 = "".join(word1)
        joined_word2 = "".join(word2)
        return True if joined_word1 == joined_word2 else False