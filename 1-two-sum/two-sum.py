class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}

        for index, num in enumerate(nums):
            num_2 = target - num
            if num_2 in dict:
                return [dict[num_2], index]
            dict[num] = index
        return []