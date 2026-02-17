class Solution:
    def isUgly(self, n: int) -> bool:
        ugly = [2, 3, 5]
        if n <= 0:
            return False        
        for elem in ugly:
            while n % elem == 0:
                n /= elem
                
        return True if n == 1 else False
