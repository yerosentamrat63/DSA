class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        sorted_s1 = sorted(s1)        
        sorted_s2 = sorted(s2)
        if sorted_s1 != sorted_s2:
            return False        
        count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
        if count == 2 or count == 0:
            return True
        else: 
            return False