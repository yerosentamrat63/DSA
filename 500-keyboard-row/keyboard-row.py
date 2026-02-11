class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        firstrow = set("qwertyuiop")
        secondrow = set("asdfghjkl")
        thirdrow = set("zxcvbnm")
        res = []

        for word in words:
            lowered = word.lower()
            if set(lowered).issubset(firstrow) or set(lowered).issubset(secondrow) or set(lowered).issubset(thirdrow):
                res.append(word)
        return res        
