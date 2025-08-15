class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        maxim = max(arr)
        maxim_ind = arr.index(maxim)

        if maxim_ind == 0 or maxim_ind == len(arr) - 1:
            return False

        for i in range(maxim_ind):
            if arr[i] >= arr[i+1]:
                return False
        for i in range(maxim_ind, len(arr)-1):
            if arr[i] <= arr[i+1]:
                return False
        return True