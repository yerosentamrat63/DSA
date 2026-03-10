class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) < k:
            return None
        window = sum(nums[:k])
        max_avg = window/k

        for i in range(len(nums)-k):
            window = window - nums[i] + nums[i+k]
            current_avg = window/k
            max_avg = max(max_avg, current_avg)

        return max_avg  