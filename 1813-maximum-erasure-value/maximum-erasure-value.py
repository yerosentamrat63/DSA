class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        sett = set()
        curr_sum = 0
        maxim = 0
        l = 0
        
        for r in range(n):
            while nums[r] in sett:
                sett.remove(nums[l])
                curr_sum -= nums[l]
                l += 1
            sett.add(nums[r])
            curr_sum += nums[r]
            maxim = max(maxim, curr_sum)
        return maxim