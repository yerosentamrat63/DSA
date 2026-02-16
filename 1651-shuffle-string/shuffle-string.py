class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        zipped = [list(subarr) for subarr in zip(indices, s)]
        zipped.sort()
        res = []
        for sub in zipped:
            res.append(sub[1])
        return ("".join(res))
        