class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        current_sum = 0
        
        for i in range(k):
            current_sum += nums[i]
        
        maxim_avg = current_sum / k

        for i in range(k, n):
            current_sum += nums[i]
            current_sum -= nums[i - k]
            current_avg = current_sum / k
            maxim_avg = max(maxim_avg, current_avg)
        return maxim_avg