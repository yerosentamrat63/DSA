class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        reverse_dict =  {v: k for k, v in count.items()}
        for n in count.values():
            if n > len(nums)/2:
                return reverse_dict[n] 