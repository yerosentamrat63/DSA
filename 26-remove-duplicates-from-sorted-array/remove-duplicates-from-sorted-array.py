class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        holder = 0
        seeker = 1

        while seeker < n:
            if nums[holder] != nums[seeker]:
                holder += 1
                nums[holder] = nums[seeker]
            seeker += 1

        return holder + 1