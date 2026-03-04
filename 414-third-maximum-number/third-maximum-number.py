class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        set_nums = set(nums)
        sorted_nums = sorted(list(set_nums))
        if len(sorted_nums) < 3:
            return sorted_nums.pop()
        return sorted_nums[-3]