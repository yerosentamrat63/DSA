class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for idx, num in enumerate(nums):
            num2 = target - num
            if num2 in res:
                return [res[num2], idx]

            res[num] = idx