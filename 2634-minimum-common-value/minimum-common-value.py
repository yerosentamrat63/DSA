class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)-1
        n = len(nums2)-1
        current_max = 0
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                m -= 1
            elif nums1[m] < nums2[n]:
                n -= 1

            elif nums1[m] == nums2[n]:
                current_max = nums1[m]
                m -= 1
                n -= 1
        if current_max == 0:
            return(-1)
        return (current_max)