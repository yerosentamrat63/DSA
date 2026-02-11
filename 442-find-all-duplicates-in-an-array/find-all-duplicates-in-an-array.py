class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        set_nums = set()
        res = []
        for i in nums:
            if i in set_nums:
                res.append(i)
            set_nums.add(i)
        return res
        