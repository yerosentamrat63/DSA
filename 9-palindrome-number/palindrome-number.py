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

"""
Space: O(1) because we only use a fixed number of variables.
Time: O(log(x)) because we divide x by 10 in each step.
"""
