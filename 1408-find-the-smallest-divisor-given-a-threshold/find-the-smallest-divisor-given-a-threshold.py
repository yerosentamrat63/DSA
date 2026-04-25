class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)

        def compute(div):
            summation = 0
            for num in nums:
                summation += (num + div - 1)//div
            return summation

        while left < right:
            mid = (left + right)//2
            if compute(mid) <= threshold:
                right = mid
            else:
                left = mid + 1
        return right