class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        leng = len(nums)
        counter = [0] * leng
        for i in range(leng):
            for j in range(leng):
                if nums[i] > nums[j]:
                    counter[i] += 1
        return(counter)

