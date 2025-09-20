class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #USED RUNNING SUM
        n = len(nums)
        l = 0
        summ = 0
        min_w = float("inf")
        for r in range(n):
            summ += nums[r]           
            while summ >= target:
                min_w = min(min_w, r - l + 1)
                summ -= nums[l]
                l += 1
        return 0 if min_w == float("inf") else min_w