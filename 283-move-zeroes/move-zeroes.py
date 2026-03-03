class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # holder = 0
        # seeker = holder + 1
        for holder in range(len(nums)):
            if nums[holder] == 0:
                for seeker in range(holder + 1, len(nums)):
                    if nums[seeker] != 0:
                        nums[holder], nums[seeker] = nums[seeker], nums[holder]
                        break
                