class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        area = 0
        left = 0
        right = n - 1
        while left < right:
            area = max(area, min(height[left],height[right]) * (abs(right - left)))
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                right -= 1
                left += 1
        return area