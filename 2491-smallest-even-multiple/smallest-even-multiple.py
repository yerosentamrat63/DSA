class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n if (n % 2 == 0) else n*2

"""
Time complexity: O(1)
Space complexity: O(1)
"""
