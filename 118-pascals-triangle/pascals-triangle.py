class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        if numRows == 0:
            return []

        initialize res = [[1]]
        shift right [0121]
        shift left  [1210]
        sum         ]1331]
        """

        res = [[1]]

        for i in range(numRows - 1):
            prev = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1]) + 1):
                row.append(prev[j] + prev[j+1])
            res.append(row)
        return res