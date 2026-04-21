class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(t):
            low = 0
            high = len(nums) -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] < t:
                    low = mid + 1
                else:
                    high = mid - 1 
            return low
        
        fo = search(target)
        lo = search(target + 1) -1
        if fo <= lo:
            return [fo, lo]
        return [-1,-1]