class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        expected = n // 4
        count = {'Q': 0, 'W': 0, 'E': 0, 'R': 0}
        
        for char in s:
            count[char] += 1
        
        if all(val == expected for val in count.values()):
            return 0
        
        left = 0
        best = n
        
        for right in range(n):
            count[s[right]] -= 1
            
            while count['Q'] <= expected and count['W'] <= expected and count['E'] <= expected and count['R'] <= expected:
                best = min(best, right - left + 1)
                count[s[left]] += 1
                left += 1
        
        return best