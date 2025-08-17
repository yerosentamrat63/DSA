class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(char for char in s if char.isalnum())
        lower_case = clean.lower()
        left = 0
        right = len(lower_case) - 1
        while left < right:
            if lower_case[left] != lower_case[right]:
                return(False)
            elif lower_case[left] == lower_case[right]:
                left += 1
                right -= 1
        return (True)