class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        new = []
        for num in arr:
            if num == 0:
                new.append(num)
                new.append(num)
                continue
            new.append(num)
        arr[:] = new[:len(arr)]