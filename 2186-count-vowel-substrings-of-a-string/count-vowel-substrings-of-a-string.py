class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        check = set('aeiou')
        count = 0

        for idx in range(len(word)):
            to_compare = set()
            for jdx in range(idx, len(word)):
                if word[jdx] not in check:
                    break
                to_compare.add(word[jdx])
                
                if len(to_compare) == 5:
                    count += 1
        return count
            