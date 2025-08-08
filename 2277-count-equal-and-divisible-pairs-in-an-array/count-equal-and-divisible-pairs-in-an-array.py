class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        dict = defaultdict(list)

        for i, num in enumerate(nums):
            for prev_i in dict[num]:
                if (i * prev_i) % k == 0:
                    count += 1
            dict[num].append(i)
        return count