class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        longest = 0
        sett = set()
        l,r = 0,0
        while r < n :
            if s[r] not in sett:
                sett.add(s[r])
                longest = max(longest,(r-l) + 1)
                r += 1
            else:
                sett.remove(s[l])
                l += 1
        return longest