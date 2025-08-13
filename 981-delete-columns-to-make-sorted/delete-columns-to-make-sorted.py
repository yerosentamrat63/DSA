class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        zipped = list(zip(*strs))
        transp = list(map(list, zipped))
        count = 0
        for i in transp[:]:
            if  i != sorted(i):
                count += 1
                transp.remove(i)
        return(count)