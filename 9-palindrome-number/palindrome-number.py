class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        temp = x
        rev = 0
        while temp:
            rev = rev * 10 + (temp % 10)
            temp //= 10
        if rev == x:
            return True
        else:
            return False 
