class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        mini = deque()
        maxim = deque()
        max_length = 0
        left = 0

        for right in range(n):
            while mini and nums[right] < mini[-1]:
                mini.pop()
            mini.append(nums[right])
            
            while maxim and nums[right] > maxim[-1]:
                maxim.pop()
            maxim.append(nums[right])
            
            while maxim[0] - mini[0] > limit:
                if nums[left] == mini[0]:
                    mini.popleft()
                if nums[left] == maxim[0]:
                    maxim.popleft()
                left += 1
                
            max_length = max(max_length, (right - left + 1))
        return max_length