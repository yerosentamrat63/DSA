class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for elem in count:
            if count[elem] == 1:
                return (s.index(elem))
                break
        return -1