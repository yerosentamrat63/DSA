class Solution:
    def threeSumClosest(self, a, t):
        a.sort()
        n = len(a)
        sol = a[0] + a[1] + a[2]
        for i in range(n - 2):
            l = i + 1
            r = n - 1
            while l < r:
                s = a[i] + a[l] + a[r]
                if abs(s - t) < abs(sol - t):
                    sol = s
                if s < t:
                    l = l + 1
                else:
                    r = r - 1
        return sol