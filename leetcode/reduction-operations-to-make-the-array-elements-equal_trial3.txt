class Solution(object):
    def reductionOperations(self, nums):
        nums.sort()
        res = 0
        count = 0

        for idx in range(1, len(nums)):
            if nums[idx] != nums[idx - 1]:
                count += 1 
            res += count
        return res