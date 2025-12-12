class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for start,end in zip(l,r):
            sub = nums[start:end+1]
            sub.sort()

            if len(sub) < 2:
                res.append(True)
                continue
            diff = sub[1] - sub[0]
            is_arithmetic = True

            for i in range(1, len(sub)):
                if sub[i] - sub[i-1] != diff:
                    is_arithmetic = False
                    break
            res.append(is_arithmetic)
        return res

            