class Solution(object):
    def reductionOperations(self, nums):
        nums.sort()
        count = 0
        temp = 0       
        for idx in range(1, len(nums)):
            if nums[idx] != nums[idx - 1]:
                temp += 1
            count += temp    
        return count