class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:        
        for row in nums:
            row.sort()
        sum = 0
        zipped = [list(i) for i in zip(*nums)]
        for arr in zipped:
            sum += max(arr)
        return sum