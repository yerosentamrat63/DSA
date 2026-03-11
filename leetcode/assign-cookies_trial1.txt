class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        hold, seek = 0,0
        count = 0
        while hold < len(g) and seek < len(s):
            if s[seek] >= g[hold]:
                count += 1
                hold += 1
                seek += 1
            else:
                seek += 1 
        return count