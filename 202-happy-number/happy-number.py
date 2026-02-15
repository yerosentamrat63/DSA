class Solution:
    def isHappy(self, n: int) -> bool:
        while len(str(n)) != 1:
            p = [int(digit) for digit in str(n)]
            n = sum(i*i for i in p)
            if sum == 1:
                return True

        if n == 1 or n== 7:
            return True
        return False