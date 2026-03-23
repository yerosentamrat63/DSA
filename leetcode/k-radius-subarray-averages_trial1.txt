class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [-1] * n
        
        window = 2 * k + 1
        if window > n:
            return res
        
        prefix = [0] * (n + 1)
        for idx in range(n):
            prefix[idx + 1] = prefix[idx] + nums[idx]
        
        for jdx in range(k, n - k):
            total = prefix[jdx + k + 1] - prefix[jdx - k]
            res[jdx] = total // window
        
        return res