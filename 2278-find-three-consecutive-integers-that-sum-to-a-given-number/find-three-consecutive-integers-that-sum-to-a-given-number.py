class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3 == 0:
            x = num // 3
            return [x - 1, x, x + 1]
        else:
            return []

"""
Time complexity: O(1)
Space complexity: O(1)
"""
