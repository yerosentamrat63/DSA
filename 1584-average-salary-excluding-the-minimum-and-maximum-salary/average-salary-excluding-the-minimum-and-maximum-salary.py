class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        remd = salary[1:-1]
        return sum(list(remd))/len(remd)