class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]

        for _ in range(rowIndex):
            newRow = []
            left = [0] + row
            right = row + [0]

            for idx in range(len(left)):
                left_val = left[idx]
                right_val = right[idx]
                newRow.append(left_val + right_val)
            row = newRow

        return row