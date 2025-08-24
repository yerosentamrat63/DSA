class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for num in nums2:
            if num in nums1:
                res.append(num)
                nums1.remove(num)
        return res