class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        n = len(arr)

        for x in range(n, 1, -1):
            idx = arr.index(x)

            if idx == x - 1:
                continue

            if idx != 0:
                res.append(idx + 1)
                arr[:idx+1] = reversed(arr[:idx+1])

            res.append(x)
            arr[:x] = reversed(arr[:x])

        return res