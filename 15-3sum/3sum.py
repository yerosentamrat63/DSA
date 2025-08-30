class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        leng = len(nums)

        i = 0
        while i < leng - 2:
            if i == 0 or nums[i] != nums[i-1]:
                l = i + 1
                r = leng - 1

                while l < r:
                    summ = nums[i] + nums[l] + nums[r]
                    
                    if summ == 0:
                        res.append([nums[i], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif summ < 0:
                        l += 1
                    else:
                        r -= 1
            i += 1
        return res