class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        zipped = list(zip(*matrix))
        return (list(map(list, zipped)))
