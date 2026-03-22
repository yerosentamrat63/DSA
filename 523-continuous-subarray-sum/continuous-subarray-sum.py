class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_storage = {0 : -1}
        prefix_sum = 0

        for idx, num in enumerate(nums):
            prefix_sum += num
            remainder = prefix_sum % k

            if remainder in remainder_storage:
                if idx - remainder_storage[remainder] >= 2:
                    return True
            else:
                remainder_storage[remainder] = idx
        return False