class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        s1_count = Counter(s1)
        n1 = len(s1)
        n2 = len(s2)
        right = n1
        left = 0
        if n1 > n2:
            return False
        while right <= n2:
            if s1_count == Counter(s2[left:right]):
                return True
            left += 1
            right += 1
        return False