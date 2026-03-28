class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        count1 = defaultdict(int)
        count2 = defaultdict(int)

        distinct_1 = 0
        distinct_2 = 0
        left1 = 0
        left2 = 0
        res = 0

        for right in range(len(nums)):
            if count1[nums[right]] == 0:
                distinct_1 += 1
            count1[nums[right]] += 1

            if count2[nums[right]] == 0:
                distinct_2 += 1
            count2[nums[right]] += 1

            while distinct_1 > k:
                count1[nums[left1]] -= 1
                if count1[nums[left1]] == 0:
                    distinct_1 -= 1
                left1 += 1

            while distinct_2 > k - 1:
                count2[nums[left2]] -= 1
                if count2[nums[left2]] == 0:
                    distinct_2 -= 1
                left2 += 1

            res += left2 - left1

        return res