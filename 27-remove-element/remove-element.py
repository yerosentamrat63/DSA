class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        left = 0

        for r in range(n):
            if nums[r] != val:
                nums[left], nums[r] = nums[r], nums[left]
                left += 1
        return left