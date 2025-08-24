class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        row = len(mat)
        summ = 0
        for i in range(row):
            summ += mat[i][i] 
        sorted_m = [i[::-1] for i in mat]
        for i in range(row):
            summ += sorted_m[i][i]
        if row % 2 != 0:
            summ -= mat[row // 2][row // 2]
        return(summ)