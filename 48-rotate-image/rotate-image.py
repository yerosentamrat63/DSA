class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        transpose = list(map(list, zip(*matrix)))

        for sub in transpose:
            sub.reverse()

        matrix[::] = transpose[::]
        