class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for idx in range(numRows - 1):
            prev = [0] + res[-1] + [0]
            subarr = []
            for jdx in range(len(res[-1])+ 1):
                subarr.append(prev[jdx] + prev[jdx+1])
            res.append(subarr)
        return res