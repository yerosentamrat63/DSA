class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        n = len(nums)
        arr = [0] * n
        
        for i in range(n - 1, -1, -1):
            arr[i] = nums[i]
            
            for j in range(i + 1, n):
                arr[j] = max(
                    nums[i] - arr[j],      # pick left
                    nums[j] - arr[j - 1]   # pick right
                )
        
        return arr[n - 1] >= 0