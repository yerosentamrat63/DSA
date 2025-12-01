class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count = 0

        val = []
        for x in nums:
            if not val or val[-1] != x:
                val.append(x)
        n = len(val)
        for i in range(1, n-1):
            if val[i] < val[i-1] and val[i] < val[i+1]:
                count += 1
            if val[i] > val[i-1] and val[i] > val[i+1]:
                count += 1
        return count