class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = [i for i in range(1, n+1)]
        i = 0
        while len(nums) > 1:
            i += k - 1
            i %= len(nums)
            nums.pop(i)
        return nums[0]