class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        new = sorted(nums)
        left = 0
        right = len(nums) - 1
        counter = 0
        while left < right:
            if new[left] + new[right] < target:
                counter += len(new[left:right])
                left += 1
            else:
                right -= 1  
        return(counter)

#better approach (O(1)) for space =>
"""
counter += (right - left)
"""