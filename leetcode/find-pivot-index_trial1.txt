class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum = 0
        rightsum = sum(nums)
        for idx, num in enumerate(nums):
            rightsum -= num
            if leftsum == rightsum:
                return idx     
            leftsum += num
        return -1