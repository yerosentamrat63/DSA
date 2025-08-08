class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100, 
            'D': 500, 
            'M': 1000
        }
        
        total = 0
        n = len(s)
        
        for i in range(n):
            current_val = roman_map[s[i]]
            
            if i + 1 < n and roman_map[s[i+1]] > current_val:
                total -= current_val
            else:
                total += current_val
        return total