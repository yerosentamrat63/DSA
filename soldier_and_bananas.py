k, n, w = map(int, input().split())
tot = 0
for i in range(1, w+1):
    tot += k*i
if n - tot < 0:
    print(tot - n)
else:
    print(0)
