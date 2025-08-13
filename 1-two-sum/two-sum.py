class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i, num in enumerate(nums):
            num_2 = target - num
            if num_2 in dic:
                return [dic[num_2], i]
            dic[num] = i