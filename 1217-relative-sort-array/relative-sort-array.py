class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        diff = list(set(arr1) - set(arr2))
        diff.sort()
        count = Counter(arr1)
        diff_arr = []
        res = []
        for elem in arr2:
            for i in range(count[elem]):
                res.append(elem)
        for num in diff:
            for j in range(count[num]):
                diff_arr.append(num)
        res.extend(diff_arr)
        return res