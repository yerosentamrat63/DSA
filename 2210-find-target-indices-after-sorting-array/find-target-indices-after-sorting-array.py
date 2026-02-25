class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        # hashmap = defaultdict(list)
        # for i in range(len(nums)):
        #     hashmap[nums[i]] += i
        if target not in nums: return []
        res = []
        count = nums.count(target)
        idx = nums.index(target)
        for i in range(count):
            res.append(idx + i)
        return res