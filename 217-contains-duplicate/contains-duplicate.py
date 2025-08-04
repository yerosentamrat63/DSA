class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = set()
        for n in nums:
            if n in dict:
                return True
            dict.add(n)
        return False

"""
Time complexity: O(n)
Space complexity: O(n)
"""
