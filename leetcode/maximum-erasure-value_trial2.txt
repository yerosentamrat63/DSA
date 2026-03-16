class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        sett = set()
        curr_summ = 0
        maxim = 0
        for right in range(n):
            while nums[right] in sett:
                sett.remove(nums[left])
                curr_summ -= nums[left]
                left += 1
            sett.add(nums[right])
            curr_summ += nums[right]
            maxim = max(curr_summ, maxim)
        return maxim