class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        min_length = float("inf")
        summ = 0
        for right in range(n):
            summ += nums[right]
            while summ >= target:
                min_length = min(min_length, right - left + 1)
                summ -= nums[left]
                left += 1
        return 0 if min_length == float("inf") else min_length