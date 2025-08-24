class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ones = 0
        zeros = 0
        twos = 0
        for i in nums:
            if i == 1:
                ones += 1
            elif i == 0:
                zeros += 1
            elif i == 2:
                twos += 1
        res = zeros * [0] + ones * [1] + twos * [2]
        nums[:] = res[:]