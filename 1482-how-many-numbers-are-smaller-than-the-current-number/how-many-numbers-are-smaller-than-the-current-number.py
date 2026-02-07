class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        rank = {}
        res = []

        for i, num in enumerate(sorted_nums):
            if num not in rank:
                rank[num] = i
        for num in nums:
            res.append(rank[num])
        return res