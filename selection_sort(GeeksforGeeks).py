class Solution: 
    def selectionSort(self, arr):
        #code here
        n = len(arr)
        for i in range(n):
            minimum_idx = i
            for j in range(i+1, n):
                if arr[j] < arr[minimum_idx]:
                    minimum_idx = j
            arr[i], arr[minimum_idx] = arr[minimum_idx], arr[i]
        return arr
