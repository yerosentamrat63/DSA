class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        count = Counter()
        maxim = 0
        sum_subarr = 0
        left = 0
        
        for right in range(len(nums)):
            count[nums[right]] += 1
            sum_subarr += nums[right]

            while count[nums[right]] > 1:
                count[nums[left]] -= 1
                sum_subarr -= nums[left]
                left += 1
            if right - left + 1 == k:
                maxim = max(sum_subarr, maxim)
                count[nums[left]] -= 1
                sum_subarr -= nums[left]
                left += 1        
        return maxim