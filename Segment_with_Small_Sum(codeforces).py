import sys
input = sys.stdin.readline

n, s = map(int, input().split())
a = list(map(int, input().split()))

left = 0
total = 0
res = 0

for right in range(n):
    total += a[right]
    while total > s:
        total -= a[left]
        left += 1
    res = max(res, right - left + 1)

print(res)
