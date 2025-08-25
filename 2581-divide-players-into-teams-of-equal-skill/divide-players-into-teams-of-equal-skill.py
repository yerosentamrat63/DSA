class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        sorted_n = sorted(skill)
        i = 0
        j = len(skill) - 1
        res = 0
        checker = sorted_n[0] + sorted_n[-1]
        while i < j:
            if sorted_n[i] + sorted_n[j] == checker:
                res += sorted_n[i] * sorted_n[j]
                i+= 1
                j -= 1
            else:
                return -1
        return(res)