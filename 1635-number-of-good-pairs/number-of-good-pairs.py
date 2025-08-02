from collections import defaultdict
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = 0
        freq = defaultdict(int)
        for num in nums:
            counter += freq[num]
            freq[num] += 1
            
        return counter