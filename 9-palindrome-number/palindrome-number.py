class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        #  converting to str

        num = str(x)
        return True if num == num[::-1] else False
        
        """
        if x < 0:
            return False
        ini_x = x
        p = x
        n = 0
        while p != 0:
            n = n * 10 + p % 10
            p //= 10

        return n == ini_x