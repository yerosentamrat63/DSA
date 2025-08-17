class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        leng = len(nums)
        counter = [0] * leng
        for i in range(leng):
            for j in range(leng):
                if nums[i] > nums[j]:
                    counter[i] += 1
        return(counter)

#Using Hashmap O(n logn)

"""
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)  
        mapping = {}
        for i, num in enumerate(sorted_nums):
            if num not in mapping:   # store only first occurrence
                mapping[num] = i
        return [mapping[num] for num in nums]
"""
