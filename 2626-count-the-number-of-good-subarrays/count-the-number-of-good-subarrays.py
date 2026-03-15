class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        same = 0
        right = -1
        count = Counter()
        res = 0
        for left in range(len(nums)):
            while same < k and right < len(nums) - 1:
                right += 1
                same += count[nums[right]]
                count[nums[right]] += 1
            if same >= k:
                res += len(nums) - right
            count[nums[left]] -= 1
            same -= count[nums[left]]
        return res