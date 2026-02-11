class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        count_nums = Counter(nums)
        for key, val in count_nums.items():
            if val > n/3:
                result.append(key)
        return result